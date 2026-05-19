import os
import json
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def _get_service():
    raw = os.environ.get('GOOGLE_CREDENTIALS_JSON')
    if not raw:
        raise ValueError("GOOGLE_CREDENTIALS_JSON environment variable is not set")
    data = json.loads(base64.b64decode(raw))
    creds = service_account.Credentials.from_service_account_info(data, scopes=SCOPES)
    return build('sheets', 'v4', credentials=creds)

def append_rows(spreadsheet_id: str, tab: str, rows: list) -> None:
    service = _get_service()
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f'{tab}!A1',
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body={'values': rows}
    ).execute()

def read_rows(spreadsheet_id: str, tab: str, range_: str = 'A:Z') -> list:
    service = _get_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{tab}!{range_}'
    ).execute()
    return result.get('values', [])

def overwrite_range(spreadsheet_id: str, tab: str, range_: str, rows: list) -> None:
    service = _get_service()
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f'{tab}!{range_}',
        valueInputOption='RAW',
        body={'values': rows}
    ).execute()
