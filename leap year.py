def leap(year):
    if((year%4==0 and year%100!=0) or year%400==0):
        print(year,"leap ")
    else:
        print(year,"not leap")
year=int(input("enter year"))
leap(year)
