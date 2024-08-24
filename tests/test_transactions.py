from src.transactions import transactions_from_csv, transactions_from_excel
import pandas as pd
from unittest.mock import patch


@patch('csv.DictReader')
def test_transactions_from_csv(mock_reader):
    mock_reader.return_value = iter([
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', '���� 58803664651298323391', '���� 39746506635466619397', '������� �����������']
    ])


assert transactions_from_csv('transactions.csv') == [
{
    "id": "650703",
    "state": "EXECUTED",
    "date": "2023-09-05T11:30:32Z",
    "amount": "16210",
    "currency_name": "SoL",
    "currency_code": "PEN",
    "from": "���� 58803664651298323391",
    "to": "���� 39746506635466619397",
    "description": "������� �����������"
}
]


@patch('pd.read_excel')
def test_transactions_from_excel(mock_reader):
    # ����������� mock_reader, ����� �� ��������� ������ ���������
    mock_reader.return_value = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "SoL",
        "currency_code": "PEN",
        "from": "���� 58803664651298323391",
        "to": "���� 39746506635466619397",
        "description": "������� �����������"
    }
]


assert transactions_from_excel('transactions.xlsx') == [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "SoL",
        "currency_code": "PEN",
        "from": "���� 58803664651298323391",
        "to": "���� 39746506635466619397",
        "description": "������� �����������"
    }
]
