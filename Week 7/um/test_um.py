
from um import count
import pytest

def test_basic_count():
    assert count("hello, um, world") == 1
    assert count("um") == 1
    assert count(" um ") == 1

def test_case_insensitivity():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, hello") == 1
    assert count("Um?") == 1

def test_substring_not_counted():
    assert count("yummy") == 0
    assert count("instrumentum") == 0
    assert count("album") == 0
    assert count("dummy") == 0

def test_multiple_occurrences():
    assert count("Um, thanks, um...") == 2
    assert count("um, um, hello, um") == 3
    assert count("um um um") == 3

def test_no_occurrences():
    assert count("hello world") == 0
    assert count("yummy yummy") == 0
    assert count("") == 0
