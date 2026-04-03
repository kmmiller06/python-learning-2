import re
text = "123 hello"
match = re.search(r"[A-Z]", text) # BUG: Pattern searches for uppercase but text has no uppercase letters   fix it
if match:
    print(f"First uppercase: {match.group()}")
else:
    print("Not found")
import re
vin = "1HGCM82633A004352"
# TODO 1: Search for the first digit in the VIN
match = re.search(r"\d", vin) # Write the re.search call
# TODO 2: Print the digit and its position using the Match object
if match:
    print(f"Digit: {match.group()}, Position: {match.start()}")
# Expected: Digit: 1, Position: 0

import re
raw_input = " SensorID: tX7-alpha "
# Step 1: Use a string method to remove leading/trailing whitespace
cleaned = raw_input.strip() # one string method call
# Step 2: Use re.search to find a lowercase letter followed by
# an uppercase letter followed by a digit (like tX7)
match = re.search(r"[a-z][A-Z]\d", cleaned)
# Replace ___ with your pattern
if match:
    print(f"Sensor tag: {match.group()}")
# Expected: Sensor tag: tX7

import re
plate = "ABC 1234"
# Write a pattern that matches an uppercase letter followed by a digit.
match = re.search(r"[A-Z][0-9]", plate) # Replace ___ with your pattern make this work
# Expected output:
# Found: C1 at position (2, 4) why is it not printing anything?     fix it
if match:
    print(f"Found: {match.group()} at position {match.span()}")
    
import re
text = "Error 42 on server-7"
m1 = re.search(r"\d", text)
print(m1.group()) # Answer: 4
m2 = re.search(r"[^a-zA-Z0-9 ]", text)
print(m2.group()) # Answer: -
print(m2.start()) # Answer: 
m3 = re.search(r"\s\w", text)
print(m3.group()) # Answer:  4