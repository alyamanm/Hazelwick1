temp = int(input("Enter your temp in celsius:"))

if temp < 0:
    print("Freezing")

elif temp > 0 and temp < 20:
     print ("Cold")

elif temp > 21 and temp <= 30:
    print ("Warm")

elif temp >=30:
     print ("Hot")