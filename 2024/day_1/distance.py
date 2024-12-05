
left_list, right_list = [], []

# Load inputs file
with open("day_1/input.txt", "r") as file:
    for line in file:
        line = line.split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

left_list.sort()
right_list.sort()

dist = 0
for i,j in zip(left_list, right_list):
    dist += abs(i-j)

print(dist)