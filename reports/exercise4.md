# Bug reports for exercise4.py

Line: 4  
Problem: Hardcoded secret password in the source code. The value "admin123" is directly stored in the code as `ADMIN_PASSWORD`, which makes it visible in version control and easily exploitable. This violates security best practices and exposes the system to unauthorized access.  
Example: If an attacker gains access to the source code, they can immediately see the admin password and use it to authenticate.  
Fix: Replace the hardcoded password with a value retrieved from environment variables. Change line 4 to: `ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")`

Line: 14  
Problem: SQL injection vulnerability in the `find_user` function due to direct string formatting in an SQL query. The username parameter is directly inserted into the SQL query using an f-string, allowing attackers to inject malicious SQL code.  
Example: An attacker could pass a username like `x' OR '1'='1` to trigger a query such as `SELECT * FROM users WHERE username = 'x' OR '1'='1'`, which would return all user rows due to the always-true condition.  
Fix: Use parameterized queries with placeholders. Replace line 14 with: `return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()`
