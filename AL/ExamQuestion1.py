C=0

while C <=8:
    height =float (input("Enter your height in centimetres: "))

    if height <140 and height >=120: 
        ans=input ("Are you with an adult?")

        if ans == "Yes":
            print ("You are allowed to ride")
            C=C+1

        else:
            print ("Cannot ride")

    elif height>=140:
        print ("You are allowed to ride!")
        C=C+1

    else:
        print ("Cannot ride")

