def leap(year):
    if year % 4 == 0:
        print 'this is leap year'
    else:
        print 'common year'
year = input("enter the year \t")
leap(year)
