def isleapyear(year: int):
    """
    The conditions for a leap year according to the Gregorian calendar are:

    - The year must be evenly divisible by 4;

    - If the year can also be evenly divided by 100,
      then it is not a leap year;

    - Unless the year is also evenly divisible by 400.
      Then it is a leap year.

    For example: 2000, 2020 are leap years;
                 But 1900, 1800 are not. 



    Return True if a year is a leap year.
    Else, return False.
    """

    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 100 == 0) and (year % 400 == 0):
        return True
    else:
        return False