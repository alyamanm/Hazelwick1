hours = -1
total = 0
while hours!= 0:
    hours=int(input("Enter hours: "))
    choice= input("Electric or Petrol: ")
    if choice =="Electric":
        total = hours*2
        print ("You have to pay",total)

    else:
        total=hours*4
        print ("You have to pay", total)