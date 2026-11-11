You must find EXACTLY 3 bugs in the provided code (one in each function). Do not stop generating until you have output 3 separate bug reports.

Look for these specific errors:
1. `is_passing`: It uses `>` instead of `>=`. Example must use 5.
2. `is_valid_password`: It uses `>` instead of `>=`. The example MUST be exactly 8 characters AND contain a digit, like "abcdefg1".
3. `clamp`: It uses `low` inside the `min()` function instead of `high`.

You MUST format each of the 3 reports EXACTLY like this:
Line: [number]
Problem: [text]
Example: [text]
Fix: [text]
