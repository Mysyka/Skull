ages = [90, 199, 21, 32, 45, 23, 16, 65, 12, 11]

minimum = ages[0]

for age in ages:
    if age < minimum:
        minimum = age

print(minimum)