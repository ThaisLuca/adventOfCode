
import re

# Load inputs file
with open("day_3/input.txt", "r") as file:
    mul = file.read()

valid_mul = re.findall("mul\(\d{1,3},\d{1,3}\)", mul)

count = 0

for val in valid_mul:
    a,b = re.findall("(\d{1,3},\d{1,3})", val)[0].split(',')
    a,b = int(a),int(b)
    count += a*b

print(count)