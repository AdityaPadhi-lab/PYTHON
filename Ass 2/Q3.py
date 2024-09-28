grade=int(input("enter the grade: "))
if(grade >90 and grade<=100):
    print("your grade is A")
    print("Excellent")
elif(grade >80 and grade<89):
    print("your grade is B")
    print("Good")
elif(grade >70 and grade<79):
    print("your grade is C")
    print("Average")
elif(grade >60 and grade<69):
    print("your grade is D")
else:
    print("your grade is F")
