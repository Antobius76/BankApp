import json
import os
from typing import Any

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "operations.json")


def fin_transactions_dict(PATH_TO_FILE: str) -> Any:
    try:
        with open(PATH_TO_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError or ValueError or FileNotFoundError:
        data = []
    return data


if __name__ == "__main__":
    print(fin_transactions_dict(PATH_TO_FILE))
