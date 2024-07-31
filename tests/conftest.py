import pytest


@pytest.fixture
def result_filter_cur():
    return [
        [
            {
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "id": 939719570,
                "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 11776614605963066702",
            },
            {
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "id": 142264268,
                "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 75651667383060284188",
            },
            {
                "date": "2018-08-19T04:27:37.904916",
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "id": 895315941,
                "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Visa Platinum 8990922113665229",
            },
        ]
    ]
