

from bank import value

def test_hello_greeting():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("hElLo") == 0
    assert value("hello123") == 0
    assert value("helloworld") == 0

def test_h_greeting():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("h") == 20
    assert value("H") == 20
    assert value("hey") == 20
    assert value("h123") == 20
    assert value("hel") == 20

def test_other_greetings():
    assert value("Goodbye") == 100
    assert value("What's up") == 100
    assert value("123") == 100
    assert value("") == 100
    assert value("a") == 100
    assert value("A") == 100
    assert value("!@#") == 100
