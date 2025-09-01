
from numb3rs import validate
import pytest

# Test valid IPv4 addresses
def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("10.1.2.3") == True

# Test invalid IPv4 addresses due to values out of range
def test_invalid_range():
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.256") == False
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False
    assert validate("-1.0.0.0") == False
    assert validate("0.0.0.255.1") == False

# Test invalid IPv4 addresses due to incorrect format
def test_invalid_format():
    assert validate("1.2.3") == False            # Too few parts
    assert validate("1.2.3.4.5") == False       # Too many parts
    assert validate("1.2.3.") == False           # Ends with dot
    assert validate(".1.2.3") == False           # Starts with dot
    assert validate("1..2.3.4") == False        # Double dot
    assert validate("cat") == False              # Not an IP
    assert validate("a.b.c.d") == False         # Non-numeric parts
    assert validate("1.2.3.dog") == False       # Mixed numeric/non-numeric
    assert validate(" 1.2.3.4 ") == False       # Leading/trailing spaces
    assert validate("1 .2.3.4") == False        # Internal space
    assert validate("1.2.3.4 ") == False        # Trailing space
    assert validate(" 1.2.3.4") == False        # Leading space
    assert validate("") == False                 # Empty string
    assert validate("...") == False              # Only dots

# Test edge cases, like single digits or valid leading zeros (which int() handles)
def test_edge_cases():
    assert validate("1.2.3.4") == True          # Single digits
    assert validate("99.99.99.99") == True      # Double digits
    assert validate("100.100.100.100") == True  # Triple digits
    assert validate("01.02.03.04") == True      # Leading zeros (valid as int() parses them)
    assert validate("192.168.0.01") == True     # Mixed leading zeros
