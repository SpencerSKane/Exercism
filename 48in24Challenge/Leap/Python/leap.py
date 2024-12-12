# Introduction

# A leap year (in the Gregorian calendar) occurs:

#    In every year that is evenly divisible by 4.
#    Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.

#Some examples:

#    1997 was not a leap year as it's not divisible by 4.
#    1900 was not a leap year as it's not divisible by 400.
#    2000 was a leap year!



def leap_year(year):

    # check if evenly divisible by 100
    if(year % 100 == 0):
        # and 400
        if(year % 400 == 0):
            return True
        else: return False

    # check if evenly divisible by 4
    elif(year % 4 == 0):
        return True
    else: return False
