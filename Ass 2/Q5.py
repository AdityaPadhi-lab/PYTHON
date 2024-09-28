year=int(input("enter the year: "))
if(year%4==0  and (year%100!=0 and year%400==0)):
    print(year, "this year is a lepa year:  ")
else:
    print(year, "this year is not a leap year")
