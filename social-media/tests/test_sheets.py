import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from unittest.mock import patch, MagicMock
from integrations.sheets import append_rows, read_rows

def _mock_service():
    svc = MagicMock()
    svc.spreadsheets.return_value.values.return_value.append.return_value.execute.return_value = {}
    svc.spreadsheets.return_value.values.return_value.get.return_value.execute.return_value = {
        'values': [['h1', 'h2'], ['v1', 'v2']]
    }
    return svc

@patch('integrations.sheets._get_service')
def test_append_rows_calls_api(mock_get):
    mock_get.return_value = _mock_service()
    append_rows('sheet123', 'Scripts', [['a', 'b']])
    mock_get.return_value.spreadsheets().values().append.assert_called_once()

@patch('integrations.sheets._get_service')
def test_read_rows_returns_values(mock_get):
    mock_get.return_value = _mock_service()
    rows = read_rows('sheet123', 'Scripts')
    assert rows == [['h1', 'h2'], ['v1', 'v2']]

@patch('integrations.sheets._get_service')
def test_read_rows_returns_empty_on_no_data(mock_get):
    svc = MagicMock()
    svc.spreadsheets.return_value.values.return_value.get.return_value.execute.return_value = {}
    mock_get.return_value = svc
    rows = read_rows('sheet123', 'Scripts')
    assert rows == []
