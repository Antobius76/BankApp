def filter_by_state(lst: list[dict], state="EXECUTED") -> list[dict]:
    """Функция прнимает список словарей и возвращает новый
    отфильтрованный по значению state список"""
    new_lst = []
    for dct in lst:
        if dct.get("state") == state:
            new_lst.append(dct)
    return new_lst


def sort_by_date(lst: list[dict], reverse: bool = True) -> list[dict]:
    """Функция прнимает список словарей и
    возвращает отсортированный по дате новый список"""
    lst.sort(key=lambda x: x["date"], reverse=reverse)
    return lst
