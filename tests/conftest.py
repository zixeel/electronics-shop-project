import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item('Вилка', 1000, 5)


@pytest.fixture
def phone():
    return Phone('Pixel', 100000, 5, 15)
