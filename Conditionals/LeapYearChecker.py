year=int(input("Enter your year:"))

if (year%400==0) or (year%4==0 and year%100!=0):
    print(year,"YES,it is leap year")

else:
    print(year,"NO,it is not a leap year")