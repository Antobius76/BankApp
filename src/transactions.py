import csv
import pandas as pd


def transactions_from_csv(filepath: str) -> list[dict]:
    """Функция принимает на вход путь до файла csv и возвращает список словарей"""
    with open(filepath, "r", encoding='latin1') as f:
        transactions_list = [{}]
        transaction_dict = csv.DictReader(f)
        for row in transaction_dict:
            transactions_list.append(row)
    return transactions_list


def transactions_from_excel(filepath: str) -> list[dict]:
    """Функция принимает на вход путь до файла Excel и возвращает список словарей"""
    transactions_list_xl = pd.read_excel(filepath)
    transactions_dict_xl = transactions_list_xl.to_dict(orient='records')
    return transactions_dict_xl
