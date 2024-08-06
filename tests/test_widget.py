import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data_, expected",
    [("Visa 4567321800123456", "Visa 4567 32** **** 3456"), ("Счет 73456285009746533245", "Счет **3245")],
)
def test_mask_account_card(data_: str, expected: str) -> None:
    assert mask_account_card(data_) == expected


@pytest.mark.parametrize("date, expected", [("2019-07-03T18:35:29.512364", "03.07.2019")])
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
