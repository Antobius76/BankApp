def filter_by_state(lst: list, state="EXECUTED") -> list | None:
    """Функция прнимает список словарей и возвращает новый
    отфильтрованный по значению state список"""

    new_lst = []
    for dct in lst:
        if dct.get("state") == state:
            new_lst.append(dict)
    return new_lst


def sort_by_date(dict_list: list, reverse: bool = True) -> list:
    sorted_dict_list = sorted(dict_list, key=lambda dct: dct.get("date"), reverse=reverse)

    return sorted_dict_list
