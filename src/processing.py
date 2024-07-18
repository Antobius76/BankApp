new_lst = []


def filter_by_state(lst: list[dict], state: bool = "EXECUTED") -> list[dict]:
    """Функция прнимает список словарей и возвращает новый
    отфильтрованный по значению state список"""

    for dct in lst:
        if dct.get("state") == state:
            new_lst.append(dct)
    return new_lst


new_list = []


def sort_by_date(lst: list[dict], reverse_list: bool = True) -> list[dict]:
    """Функция прнимает список словарей и
    возвращает отсортированный по дате новый список"""
    sorted_list = sorted(lst, key=lambda x: x["date"], reverse=reverse_list)
    new_list.append(sorted_list)
    return sorted_list
