import os
import re
from collections import Counter

from utils import fin_transactions_dict

list_transactions = fin_transactions_dict(os.path.join("../data/operations.json"))


def list_dict_with_transaction(list_dict: list, search_str: str) -> list:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    new_list = []
    for transaction in list_dict:
        if "description" in transaction and re.findall(search_str, transaction["description"]):
            new_list.append(transaction)
    return new_list


def count_categories(list_dict_trans: list, categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_categories_transaction = []
    for transaction in list_dict_trans:
        if "description" in transaction and transaction["description"] in categories:
            list_categories_transaction.append(transaction["description"])
    sorted_transaction = Counter(list_categories_transaction)
    return dict(sorted_transaction)
