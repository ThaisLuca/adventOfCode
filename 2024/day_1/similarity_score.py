
left_list, right_list = [], []

# Load inputs file
with open("day_1/input.txt", "r") as file:
    for line in file:
        line = line.split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

similarity_score = 0
for i in left_list:
    mult = list.count(right_list,i)
    similarity_score += i * mult

print(similarity_score)