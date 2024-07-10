from typing import Any


def get_mask_card(card_num: str) -> Any:
    """Функция возвращает маску номера карты"""

    if card_num.isdigit() and len(card_num) == 16:
        return f"{card_num[:5]} {card_num[5:7]}** **** {card_num[12:]}"
    else:
        return None


def get_mask_account(acc_num: str) -> Any:
    """Функция возвращает маску номера счета"""

    if acc_num.isdigit() and len(acc_num) == 20:
        return f"**{acc_num[-4::]}"
    else:
        None
