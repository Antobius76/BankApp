from unittest.mock import patch
from src.external_api import transaction_amount


@patch('requests.get')
def test_transaction_amount(mock_currency):
    mock_currency.return_value = 735388.41697211
    assert transaction_amount({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }) == 735388.41697211
