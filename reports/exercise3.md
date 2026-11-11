# Bug reports for exercise3.py

Line: 3
Problem: The function `average` raises a `ZeroDivisionError` when the input list is empty because `len(numbers)` would be 0, leading to division by zero. According to the docstring, an empty list should have an average of 0.
Example: average([])
Fix: Replace `return sum(numbers) / len(numbers)` with `return sum(numbers) / len(numbers) if numbers else 0`

Line: 8
Problem: The function `first_word` raises an `IndexError` when the input text is empty because `text.split()[0]` attempts to access the first element of an empty list after splitting an empty string.
Example: first_word("")
Fix: Replace `return text.split()[0]` with `return text.split()[0] if text.split() else ""`

Line: 13
Problem: The function `percent` raises a `ZeroDivisionError` when `total` is 0 because it divides `part` by `total`, which results in division by zero. According to the docstring, if `total` is 0, the result should be 0.
Example: percent(1, 0)
Fix: Replace `return part / total * 100` with `return part / total * 100 if total != 0 else 0`
