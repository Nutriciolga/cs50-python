from bank import value


def test_1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0


def test_2():
    assert value("hi") == 20


def test_3():
    assert value("moi") == 100