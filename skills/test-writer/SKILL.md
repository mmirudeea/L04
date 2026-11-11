Output ONLY Python code. No markdown or explanations. Write exactly one test function.

If the report is about ADMIN_PASSWORD, output EXACTLY this:
def test_admin_password_is_secure():
    assert ADMIN_PASSWORD != "admin123"

If the report is about SQL injection, output EXACTLY this:
def test_sql_injection_prevented():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('ana')")
    assert find_user(db, "x' OR '1'='1") is None
