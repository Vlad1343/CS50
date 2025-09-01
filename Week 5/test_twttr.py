from twttr import shorten

def test_shorten_removes_vowels():
    assert shorten("Hello") == "Hll"
    assert shorten("AEIOU") == ""
    assert shorten("aEiOu") == ""
    assert shorten("Python") == "Pythn"

def test_shorten_keeps_consonants():
    assert shorten("BCDFG") == "BCDFG"
    assert shorten("xyz") == "xyz"
    assert shorten("qrst") == "qrst"

def test_shorten_handles_mixed_input():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("123abcXYZ!") == "123bcXYZ!"
    assert shorten("A1B2C3") == "1B2C3"

def test_shorten_edge_cases():
    assert shorten("") == ""
    assert shorten("aaaaa") == ""
    assert shorten("BBB") == "BBB"
    assert shorten("aeiouy") == "y"
