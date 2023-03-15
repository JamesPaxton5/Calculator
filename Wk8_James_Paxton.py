# This is the flower box and it should at the beginning of each assignment

# You must add comments to your code
# Program name : Wk8_James_Paxton.py
# Student Name : James Paxton
# Course : ENTD220
# Instructor : Ahmed Abaza
# Date : 9/24/22

# Copy Wrong: This is my work
# the two Error Traps begin on line 33 and 50 (week 4 assignment)
# line 33 trap is setup to stop the user from entering anything other than a number and will inform them on this error/requirment
# line 55 trap is a divide by zero. If the user tries to divide by zero the message will let them know that it cant be done. 

while True:

    import Wk8_James_Paxton_MyLib

    #created an object from the class
    iCalc = Wk8_James_Paxton_MyLib.calc()
    iFile = Wk8_James_Paxton_MyLib.wrfile()

    #this is the lr and hr set limits
    lr = -80
    hr = 90

    #This is setup as a trap error for Values, If the user types in a letter it will inform them that they can only use numbers.
    try:
        #Did this with the help wiht you on zoom. This lines show input for the Users range
        ulr=int( input("enter user lower range between "+str(lr)+" and "+str(hr)+": "))
    except ValueError:
        print("Numbers only")
        continue
    else:
        uhr=int( input("enter user high range between "+str(lr)+" and "+str(hr)+": "))
        #this checks to make sure the user has picked something in between the set ranges.
        if(iCalc.checknum(lr,ulr,hr) and iCalc.checknum(lr,uhr,hr)):
            n1=int( input("enter user first number "+str(ulr)+" and "+str(uhr)+": "))
            n2=int( input("enter user second number "+str(ulr)+" and "+str(uhr)+": "))
            operation = str(input("Enter problem sting like this "+"Number1,Number2,Operator: "))

        #"if" everything is inputed right it will print answers. if not it will make user pick another input within the range
            if(iCalc.checknum(ulr,n1,uhr) and iCalc.checknum(ulr,n2,uhr)):
                print("The Result will be "+str(float(iCalc.scalc((operation)))))
                print("The Result of "+str(n1)+" + "+str(n2)+" = "+str(float(iCalc.add(n1,n2))))
                print("The Result of "+str(n1)+" - "+str(n2)+" = "+str(float(iCalc.subtract(n1,n2))))
                print("The Result of "+str(n1)+" * "+str(n2)+" = "+str(float(iCalc.multiply(n1,n2))))
                try:
                    print("The Result of "+str(n1)+" / "+str(n2)+" = "+str(float(iCalc.divide(n1,n2))))
                #If you user inputted a "0" it would bring an error up. so I have coded a Zero division error code in so that if the user does try using "0" it is run/print "can't divide by zero"
                except ZeroDivisionError:
                    print("The Result of "+str(n1)+" / "+str(n2)+" = Can't divide by zero")
            else:
                print("Please check the numbers and try again")
        else:
            print("The input values are outside the input ranges")
        if __name__ == "__main__":
            iCalc.main()
        #If answered "yes" the program will repeat and if answered "no" it will end
        repeat=input("Continue Looping yes or no? ")
        if repeat=="yes":
            continue
        else:
            print("Thanks for using our calculator ")
            break