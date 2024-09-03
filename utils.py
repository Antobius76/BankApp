import json
import logging
import os
from typing import Any

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "operations.json")


def fin_transactions_dict(PATH_TO_FILE: str) -> Any:
    try:
        with open(PATH_TO_FILE, "r", encoding="utf-8") as f:
            logger.info("Открывается файл")
            data = json.load(f)
    except json.JSONDecodeError or ValueError or FileNotFoundError:
        logger.error("Ошибка файла")
        data = []
    return data


if __name__ == "__main__":
    print(fin_transactions_dict(PATH_TO_FILE))
    logger.info("Данные записываются в файл")
