from plates import is_valid

def test_length():
    # Valid lengths
    assert is_valid("AB") is True
    assert is_valid("ABCD") is True
    assert is_valid("ABCDEF") is True
    # Invalid lengths
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False

def test_first_two_letters():
    # Valid first two letters
    assert is_valid("AB") is True
    assert is_valid("Ab123") is True  # case-insensitive
    # Invalid first two letters
    assert is_valid("A1") is False
    assert is_valid("1A") is False
    assert is_valid("12") is False

def test_alphanumeric():
    # Valid alphanumeric
    assert is_valid("AB123") is True
    # Invalid characters
    assert is_valid("AB@12") is False
    assert is_valid("AB 12") is False
    assert is_valid("AB.12") is False
    assert is_valid("AB,12") is False

def test_numbers_at_end():
    # Valid numbers at end
    assert is_valid("AB123") is True
    assert is_valid("AB1") is True
    assert is_valid("AB10") is True
    # Invalid numbers (middle)
    assert is_valid("AB1C") is False
    assert is_valid("AB12C") is False
    # First number is zero
    assert is_valid("AB01") is False
    assert is_valid("AB00") is False
    # Zero in middle but first number is not zero (but letters after)
    assert is_valid("AB10C") is False
    # Edge case: all numbers after first two letters
    assert is_valid("AB0") is False  # first number is zero
    assert is_valid("AB0123") is False  # first number is zero
    # Valid: numbers after letters, all digits
    assert is_valid("ABC123") is True
    # Invalid: letters after digits
    assert is_valid("ABC12D") is False
