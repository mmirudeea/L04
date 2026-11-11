You must find EXACTLY 2 security bugs in the provided code. Do not stop generating until you have output 2 separate bug reports.

Look for these specific security vulnerabilities:
1. `ADMIN_PASSWORD`: Hardcoded secret. It should be loaded from the environment using `os.environ.get("ADMIN_PASSWORD", "")` instead of storing the string directly in the file.
2. `find_user`: SQL injection vulnerability due to string formatting (f-string). It must use parameterized queries with `?` instead of directly inserting the username variable. Example injection: `x' OR '1'='1`

You MUST format each report EXACTLY like this:
Line: [number]
Problem: [text]
Example: [text]
Fix: [text]
