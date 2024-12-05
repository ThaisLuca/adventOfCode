
import re

# Load inputs file
with open("day_3/input.txt", "r") as file:
    mul = file.read()

count = 0

while mul:
    # Search for mul(XX,XX) expression
    index_mul = re.search("mul\(\d{1,3},\d{1,3}\)", mul)

    # If no more mul expressions, there is no need to continue
    if not index_mul:
        break

    # Collect mul expression indexes
    index_mul_start = index_mul.start()
    index_mul_end = index_mul.end()

    # Search for some don't() operator
    index_dont = re.search("don't\(\)", mul)

    # If find it, collect indexes
    if index_dont:
        index_dont_start = index_dont.start()
        index_dont_end = index_dont.end()

    # If there is no don't() operator or don't() operator indexes is greater than mul expression index, there is no block
    if not index_dont or index_dont_start > index_mul_start:
        val = mul[index_mul_start:index_mul_end]
        a,b = re.findall("(\d{1,3},\d{1,3})", val)[0].split(',')
        a,b = int(a),int(b)
        count += a*b

        # Update string to remove current mul expression
        mul = mul[:index_mul_start] + mul[index_mul_end:]
    
    else:

        # In case of a don't() in front the mul expression, search for a do()
        mul = mul[index_dont_end:]
        index_do = re.search("do\(\)", mul)

        # If there is no do(), there is nothing we can do
        if not index_do:
            break

        # Collect indexes and update string to start from the do() expression
        index_do_start = index_do.start()
        index_do_end = index_do.end()

        mul = mul[index_do_start:]

print(count)