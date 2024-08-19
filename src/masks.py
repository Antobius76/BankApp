import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card(card_num: str) -> str | None:
    """Функция возвращает маску номера карты"""

    if card_num.isdigit() and len(card_num) == 16:
        logger.info("Маскируется номер карты")
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    else:
        return None


def get_mask_account(acc_num: str) -> str | None:
    """Функция возвращает маску номера счета"""

    if len(acc_num) == 20:
        logger.info("Маскируется номер счета")
        return f"**{acc_num[-4::]}"
    else:
        return None


get_mask_card("1323423243999900")
get_mask_account("12909998282838383939")
