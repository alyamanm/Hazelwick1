days = int(input("How many days? "))

total = 0

for i in range(days):
    temp = (input("Enter temperature: "))
    total=temp

average = total / days

print("Average temperature:", average)