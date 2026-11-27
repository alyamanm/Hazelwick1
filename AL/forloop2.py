days = int(input("How many days? "))

frosty = 0
total = 0
highest = 0

for i in range(days):
    temp = int(input("Enter temperature: "))
    total = total + temp

    if temp > highest:
        highest = temp

    if temp < 0:
        frosty = frosty + 1

average = total / days

print("Average temperature:", average)
print("Highest temperature:", highest)
print("Frosty days:", frosty)