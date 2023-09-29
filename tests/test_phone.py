

def test_str(phone):
    assert str(phone) == 'Pixel'


def test_repr(phone):
    assert repr(phone) == "Phone('Pixel', 100000, 5, 15)"


def test_number_of_sim(phone):
    assert phone.number_of_sim == 15

