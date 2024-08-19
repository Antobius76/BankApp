import pytest

from src.masks import get_mask_account, get_mask_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("4003345612657812", "4003 34** **** 7812"),
    ],
)
def test_get_mask_card(number: str, expected: str) -> None:
    assert get_mask_card(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("34564321567843215678", "**5678"),
    ],
)
def test_get_mask_account(number: str, expected: str) -> None:
    assert get_mask_account(number) == expected
