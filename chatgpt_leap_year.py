def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
#Input year
year = int(input("Pls enter year"))
if is_leap_year(year):
    print("It's a leap year.")
else:
    print("Not a leap year.")


