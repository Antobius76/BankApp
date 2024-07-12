from src.masks import get_mask_account, get_mask_card


def mask_account_card(number: str) -> str:
    """Функция принимает название и номер карты или
    номер счета и возвращает их маску"""
    if "Счет" in number:
        return f"Счет {get_mask_account(number[-20:])}"
    else:
        card = number[:-16]
        return f"{card} {get_mask_card(number[-16:])}"


def get_date(info: str) -> str:
    """Функция принимает строку, содержащую дату
    и возвращает в формате дд.мм.гггг."""
    date = info[:10]
    return f"{date[8:11]}.{date[5:7]}.{date[0:4]}"
