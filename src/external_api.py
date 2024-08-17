import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_amount(transaction: dict) -> float:
    amount_sum = transaction["operationAmount"]["amount"]
    cur_code = transaction["operationAmount"]["currency"]["code"]
    if cur_code == "RUB":
        return amount_sum
    elif cur_code == "USD" or cur_code == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={cur_code}&amount={amount_sum}"
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)
        result = response.json()
        return result["result"]


if __name__ == "__main__":
    print(
        transaction_amount(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
    )
