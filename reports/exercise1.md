# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For an even number, the remainder when divided by 2 should be 0, not 1. This causes the function to return `True` for odd numbers and `False` for even numbers, which is the opposite of the intended behavior.
Example: is_even(4) should return True (since 4 is even), but it returns False because 4 % 2 == 0, not 1.
Fix: return n % 2 == 0

Line: 8
Problem: The function `rectangle_area` incorrectly returns the sum of width and height instead of the product (area of a rectangle). The area of a rectangle is calculated as width multiplied by height, not added.
Example: rectangle_area(5, 3) should return 15, but it returns 8.
Fix: return width * height

Line: 13
Problem: The function `double(n)` adds 2 to the input instead of multiplying it by 2. The term "twice" means multiplication by 2, not addition.
Example: double(5) should return 10, but it returns 7.
Fix: return n * 2
