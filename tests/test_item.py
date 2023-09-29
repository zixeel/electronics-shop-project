"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_name(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item):
    assert repr(item) == "Item('Вилка', 1000, 5)"


def test_str(item):
    assert str(item) == 'Вилка'


def test_add(item, phone):
    assert item + phone == 10
    assert phone + phone == 10
