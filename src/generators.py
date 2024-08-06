def filter_by_currency(transactions: list[dict], currency: str = "USD"):
    """Функция выдает транзакции, где валюта операции соответствует заданной."""
    try:
        for i in transactions:
            if i.get("operationAmount").get("currency").get("code") == currency:
                yield i
    except StopIteration:
        if not transactions:
            return "Нет транзакций"


def transaction_descriptions(transactions: list[dict]):
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for descr in transactions:
        try:
            yield descr.get("description")
        except StopIteration:
            if not transactions:
                return "Нет транзакций"


def card_number_generator(start: int, stop: int):
    """Функция может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
