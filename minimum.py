ages = [90, 199, 21, 32, 45, 23, 2, 65, 12, 1]

minimum = ages[0]

for age in ages:
    if age < minimum:
        minimum = age

print(minimum)