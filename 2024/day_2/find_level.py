
def load_data(filename):
    reports = []

    # Load inputs file
    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            reports.append([int(i) for i in line])
    return reports

def check_is_safe(report):

    # check if increases or decreases
    if report == sorted(report, reverse=True) or report == sorted(report):

        for i in range(len(report)-1):
            
            if i == len(report):
                break

            a = report[i]
            b = report[i+1]
            diff = abs(a-b)

            if diff > 3 or diff < 1:
                return False
    else:
        return False

    return True


reports = load_data("day_2/input.txt")

safe_reports = 0
for report in reports:

    if check_is_safe(report):
        safe_reports += 1
    else:
        for j in range(len(report)):
            n_report = report[:j] + report[j+1:]
            if check_is_safe(n_report):
                safe_reports += 1
                break

print(safe_reports)  