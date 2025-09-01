
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    try:
        Jar(-1)
    except ValueError as e:
        assert str(e) == "Capacity must be a non-negative integer."
    else:
        assert False, "Expected ValueError not raised"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    assert Jar().capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5
    jar.deposit(5)
    assert jar.size == 5

def test_deposit_exceeds_capacity():
    jar = Jar(5)
    jar.deposit(5)
    try:
        jar.deposit(1)
    except ValueError as e:
        assert str(e) == "Exceeds capacity."
    else:
        assert False, "Expected ValueError not raised"


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0

def test_withdraw_not_enough_cookies():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(5)
    try:
        jar.withdraw(1)
    except ValueError as e:
        assert str(e) == "Not enough cookies."
    else:
        assert False, "Expected ValueError not raised"
