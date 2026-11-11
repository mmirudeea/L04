# Bug reports for exercise2.py

Line: 3  
Problem: The function `is_passing` should return `True` if the grade is 5 or more, but it uses `>` which means it will return `False` for a grade of exactly 5. It should use `>=` to include 5.  
Example: For a grade of 5, the function currently returns `False`, but it should return `True`.  
Fix: Change `return grade > 5` to `return grade >= 5`

Line: 8  
Problem: The function `is_valid_password` requires at least 8 characters, but it uses `>` which means it will reject passwords of exactly 8 characters. It should use `>=` to include 8-character passwords.  
Example: The password "abcdefg1" has exactly 8 characters and contains a digit, so it should be valid, but the function currently returns `False`.  
Fix: Change `return len(password) > 8 and any(c.isdigit() for c in password)` to `return len(password) >= 8 and any(c.isdigit() for c in password)`

Line: 13  
Problem: The `clamp` function incorrectly uses `low` inside the `min(x, low)` call, which makes it always return `low` regardless of `x`. It should compare `x` with `high` to ensure it doesn't exceed `high`.  
Example: For `x=10`, `low=1`, `high=5`, the function returns `max(1, min(10, 1)) = 1`, but it should return `5` because `x` exceeds `high`.  
Fix: Change `return max(low, min(x, low))` to `return max(low, min(x, high))`
