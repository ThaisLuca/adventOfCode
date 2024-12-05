reports = []

# Load inputs file
with open("day_2/input.txt", "r") as file:
    for line in file:
        line = line.split()
        reports.append([int(i) for i in line])

safe_reports = 0
for report in reports:
    is_safe = True

    # check if increases or decreases
    if report == sorted(report, reverse=True) or report == sorted(report):

        for i in range(len(report)-1):
            
            if i == len(report):
                break

            a = report[i]
            b = report[i+1]
            diff = abs(a-b)
            if diff > 3 or diff < 1:
                is_safe = False
                break
    else:
        is_safe = False
    
    if is_safe:
        safe_reports += 1

print(safe_reports)  