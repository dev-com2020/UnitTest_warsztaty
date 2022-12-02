LIST = [1, 2, 3]


def test_one():
    pass


def test_two():
    assert 2 == 1 + 1


def test_three():
    assert 3 in LIST

def test_czy_4_nie_ma_w_liscie():
    assert 4 not in LIST
