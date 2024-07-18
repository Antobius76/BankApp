def get_mask_card(card_num: str) -> str | None:
    """Функция возвращает маску номера карты"""

    if card_num.isdigit() and len(card_num) == 16:
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    else:
        return None


def get_mask_account(acc_num: str) -> str | None:
    """Функция возвращает маску номера счета"""

    if len(acc_num) == 20:
        return f"**{acc_num[-4::]}"
    else:
        return None
