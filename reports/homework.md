# Bug reports for homework.py

Line: 3
Problem: The function attempts to subtract a string ("!") from the input text, which is not valid for strings in Python. String subtraction is undefined and will raise a TypeError.
Example: add_exclamation("hello") → TypeError: unsupported operand type(s) for -: 'str' and 'str'
Fix: return text + "!"

Line: 7
Problem: The function returns True if the number is greater than or equal to zero, but the requirement specifies "strictly greater than 0". This means non-positive numbers (including zero) are incorrectly classified as positive.
Example: is_positive(0) → True (should be False)
Fix: return number > 0

Line: 11
Problem: The function returns items[-1] without checking if the list is empty. If the list is empty, items[-1] will raise an IndexError.
Example: get_last_item([]) → IndexError: list index out of range
Fix: return items[-1] if items else None

Line: 15
Problem: The default argument my_list=[] is evaluated only once when the function is defined, not each time it is called. This causes all calls to append to the same list, leading to unintended side effects.
Example: add_to_list("a", []) → ['a'], add_to_list("b", []) → ['a', 'b'] (unexpected shared list)
Fix: change default argument to None and create a new list inside the function: my_list = my_list if my_list else []

Line: 20
Problem: The discount calculation is incorrect. It adds 100 to the discount_percent instead of subtracting it. The correct formula should be price * (1 - discount_percent / 100), not price * (discount_percent + 100).
Example: calculate_discount(100, 20) → -1000 (incorrect)
Fix: return price - (price * (discount_percent / 100))
