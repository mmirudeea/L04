import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_add_exclamation():
    assert add_exclamation("hello") == "hello!"


# bug report 2
def test_r2_is_positive():
    assert is_positive(0) == False


# bug report 3
def test_r3_get_last_item_empty_list():
    assert get_last_item([]) is None


# bug report 4
def test_r4_add_to_list():
    """Test that add_to_list creates a new list each time and doesn't share state."""
    result1 = add_to_list("a")
    result2 = add_to_list("b")
    assert result1 == ["a"] and result2 == ["b"], "Function should create new lists each time"


# bug report 5
def test_r5_calculate_discount():
    assert calculate_discount(100, 20) == 80
