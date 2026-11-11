import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_admin_password_is_secure():
    assert ADMIN_PASSWORD != "admin123"


# bug report 2
def test_r2_sql_injection_prevented():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('ana')")
    assert find_user(db, "x' OR '1'='1") is None
