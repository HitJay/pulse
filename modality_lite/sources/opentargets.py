from __future__ import annotations

import json
import urllib.error
import urllib.request

from modality_lite.models import TargetFeatures


API_URL = "https://api.platform.opentargets.org/api/v4/graphql"

SEARCH_QUERY = """
query Search($queryString: String!) {
  search(queryString: $queryString, entityNames: ["target"], page: {index: 0, size: 5}) {
    hits { id name entity }
  }
}
"""

TARGET_QUERY = """
query Target($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    id
    approvedSymbol
    approvedName
    biotype
    tractability { modality label value }
  }
}
"""


class OpenTargetsError(RuntimeError):
    pass


def graphql(query: str, variables: dict[str, object] | None = None, timeout: int = 30) -> dict[str, object]:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise OpenTargetsError(f"OpenTargets request failed: {exc}") from exc

    if data.get("errors"):
        raise OpenTargetsError(json.dumps(data["errors"], ensure_ascii=False))
    return data["data"]


def find_target_id(symbol: str) -> tuple[str, list[dict[str, object]]]:
    data = graphql(SEARCH_QUERY, {"queryString": symbol})
    hits = data["search"]["hits"]
    exact = [hit for hit in hits if str(hit["name"]).upper() == symbol.upper()]
    hit = exact[0] if exact else (hits[0] if hits else None)
    if not hit:
        raise OpenTargetsError(f"No OpenTargets target found for {symbol!r}")
    return str(hit["id"]), hits


def fetch_target_features(symbol: str) -> TargetFeatures:
    ensembl_id, _ = find_target_id(symbol)
    data = graphql(TARGET_QUERY, {"ensemblId": ensembl_id})
    target = data["target"]
    tractability: dict[str, set[str]] = {}
    for row in target.get("tractability") or []:
        if row.get("value"):
            tractability.setdefault(str(row["modality"]), set()).add(str(row["label"]))

    return TargetFeatures(
        symbol=str(target.get("approvedSymbol") or symbol).upper(),
        ensembl_id=str(target.get("id") or ensembl_id),
        approved_name=target.get("approvedName"),
        biotype=target.get("biotype"),
        tractability=tractability,
        source_url=f"https://platform.opentargets.org/target/{ensembl_id}",
    )