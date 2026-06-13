import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dotenv import load_dotenv
from integrations.sheets import _get_service, read_rows

load_dotenv()


def inspect(spreadsheet_id: str) -> None:
    service = _get_service()
    metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    print(f"Spreadsheet title: {metadata.get('properties', {}).get('title', '')}")
    print(f"Spreadsheet URL: https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit")

    for sheet in metadata.get("sheets", []):
        props = sheet.get("properties", {})
        title = props.get("title", "")
        rows = read_rows(spreadsheet_id, title, "A1:Z20")
        print(f"{title}: {len(rows)} populated row(s)")
        if rows:
            print(f"  First row: {rows[0]}")
        if len(rows) > 1:
            print(f"  Second row: {rows[1]}")


if __name__ == "__main__":
    sid = os.environ.get("SPREADSHEET_ID") or sys.argv[1]
    inspect(sid)
