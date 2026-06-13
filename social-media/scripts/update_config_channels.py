import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dotenv import load_dotenv
from integrations.sheets import overwrite_range, read_rows
from integrations.youtube import _get_service

load_dotenv()

SEARCH_QUERIES = {
    "Kenya Red Cross": "Kenya Red Cross Society official",
    "SHOFCO": "SHOFCO Shining Hope for Communities official",
    "UNICEF Kenya": "UNICEF Kenya official",
    "Amref Health": "Amref Health Africa official",
    "GlobalGiving": "GlobalGiving official",
}

HANDLE_CANDIDATES = {
    "Kenya Red Cross": ["KenyaRedCrossSociety", "KenyaRedCross"],
    "SHOFCO": ["SHOFCO"],
    "UNICEF Kenya": ["UNICEFKenya"],
    "Amref Health": ["AmrefHealthAfrica"],
    "GlobalGiving": ["GlobalGiving"],
}


def _normalize(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def _tokens(value: str) -> list[str]:
    cleaned = "".join(ch.lower() if ch.isalnum() else " " for ch in value)
    return [token for token in cleaned.split() if token]


def _score_candidate(row_name: str, title: str) -> int:
    normalized_name = _normalize(row_name)
    normalized_title = _normalize(title)
    score = 0
    if normalized_name in normalized_title:
        score += 20
    for token in _tokens(row_name):
        if token and token in normalized_title:
            score += 2
    if "official" in normalized_title:
        score += 3
    return score


def _channel_from_handle(service, handle: str) -> tuple[str, str] | None:
    response = service.channels().list(
        part="snippet",
        forHandle=f"@{handle}",
    ).execute()
    items = response.get("items", [])
    if not items:
        return None

    item = items[0]
    channel_id = item.get("id", "")
    title = item.get("snippet", {}).get("title", "")
    if channel_id.startswith("UC"):
        return channel_id, title
    return None


def resolve_channel_id(row_name: str, query: str) -> tuple[str, str]:
    """Resolve a YouTube channel ID and title from handles, then search as fallback."""
    service = _get_service()
    for handle in HANDLE_CANDIDATES.get(row_name, []):
        resolved = _channel_from_handle(service, handle)
        if resolved:
            return resolved

    response = service.search().list(
        part="snippet",
        q=query,
        type="channel",
        maxResults=5,
    ).execute()

    candidates = []
    for item in response.get("items", []):
        channel_id = item.get("id", {}).get("channelId", "")
        title = item.get("snippet", {}).get("title", "")
        if channel_id.startswith("UC"):
            candidates.append((_score_candidate(row_name, title), channel_id, title))

    if not candidates:
        raise ValueError(f"No YouTube channel found for {row_name!r} using query {query!r}")

    candidates.sort(reverse=True)
    _, channel_id, title = candidates[0]
    return channel_id, title


def update_config(spreadsheet_id: str) -> list[list[str]]:
    """Replace placeholder channel IDs in the Config tab."""
    rows = read_rows(spreadsheet_id, "Config", "A1:D")
    if len(rows) < 2:
        raise ValueError("Config tab has no data rows. Run setup_sheets.py first.")

    header, data_rows = rows[0], rows[1:]
    updated_rows = []

    for row in data_rows:
        padded = (row + ["", "", "", ""])[:4]
        name, platform, channel_id, notes = padded

        if platform.strip().lower() == "youtube" and name in SEARCH_QUERIES:
            query = SEARCH_QUERIES.get(name, notes or name)
            resolved_id, resolved_title = resolve_channel_id(name, query)
            channel_id = resolved_id
            notes = f"Resolved: {resolved_title}"
            print(f"{name}: {resolved_title} -> {channel_id}")

        updated_rows.append([name, platform, channel_id, notes])

    overwrite_range(spreadsheet_id, "Config", f"A2:D{len(updated_rows) + 1}", updated_rows)
    return [header, *updated_rows]


if __name__ == "__main__":
    sid = os.environ.get("SPREADSHEET_ID") or sys.argv[1]
    update_config(sid)
