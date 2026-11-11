You must find EXACTLY 3 bugs in the provided code (one in each function). Do not stop generating until you have output 3 separate bug reports.

Look for these specific edge-case crash errors:
1. `average`: Raises ZeroDivisionError if the list is empty. It should return 0 instead. Example input: []
2. `first_word`: Raises IndexError if the text is empty. It should return "" instead. Example input: ""
3. `percent`: Raises ZeroDivisionError if total is 0. It should return 0 instead. Example input: 1, 0

You MUST format each of the 3 reports EXACTLY like this:
Line: [number]
Problem: [text]
Example: [text]
Fix: [text]
