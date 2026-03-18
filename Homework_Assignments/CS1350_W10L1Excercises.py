#beginner
print("Beginner: Search for patters")
import re
text = "My student ID is s12345 and my room is B204"
# TODO 1: Use re.search to find a single digit anywhere in the text
match = None
if match:
print(f"First digit: {match.group()}")
print(f"Found at position: {match.start()}")
# TODO 2: Search for an uppercase letter followed by a digit (like B2)
match2 = None
if match2:
print(f"Letter-digit pair: {match2.group()}")
print(f"Span: {match2.span()}")
# TODO 3: Search for "s" followed by exactly 5 digits (the student ID)
match3 = None
if match3:
print(f"Student ID: {match3.group()}")

#intermediate
print("Intermediate: Character type detective")
import re
samples = [
"Room A3 is open",
"Call 5551234 now",
"hello world",
"ERROR: code 42",
]
for text in samples:
print(f"\nAnalyzing: '{text}'")
# TODO 1: Search for an uppercase letter followed by a digit
# Hint:
upper_digit = None
if upper_digit:
print(f" Upper+digit pair: '{upper_digit.group()}' at
{upper_digit.span()}")
# TODO 2: Search for a digit followed by a lowercase letter
# Hint:
digit_lower = None
if digit_lower:
print(f" Digit+lower pair: '{digit_lower.group()}' at
{digit_lower.span()}")
# TODO 3: Search for a space followed by a non-space character
# Hint:
space_nonspace = None
if space_nonspace:
print(f" Space boundary at position: {space_nonspace.start()}")
# TODO 4: Search for any character that is NOT a letter or digit
# Hint:
special = None
if special:
print(f" Special char: '{special.group()}' at {special.start()}")
else:
print(f" No special characters found")

#advanced
print("Advanced: Date stamp finder")
import re
log_lines = [
"2026-03-10 INFO Server started on port 8080",
"2026-03-10 ERROR Connection refused",
"no date here, just a message",
"2026-03-11 WARN Memory usage high",
]
for line in log_lines:
# TODO 1: Search for a date stamp: 4 digits, dash, 2 digits, dash, 2 digits
# Use only \d and literal dashes
date_match = None
# TODO 2: Search for "ERROR" as a literal string
is_error = re.search(r"ERROR", line)
# TODO 3: Search for a 4-digit number (digit NOT preceded/followed by dash)
port_match = None
# Build output
if date_match:
date_str = date_match.group()
rest = line[date_match.end():]
status = "ERROR" if is_error else "ok "
port = port_match.group().strip() if port_match else "n/a"
print(f"[{date_str}] {status} | port: {port} | {rest.strip()}")
else:
print(f"[no date ] skipped | {line}")