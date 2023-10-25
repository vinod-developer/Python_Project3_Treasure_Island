print("Welcome to Roller Coaster Ride")
height = int(input("please enter your height in cms\n"))
bill = 0
if height >= 120:
    age = int(input("Please enter your age"))
    if (age > 45 and age < 55):
        bill = 0
    elif age <= 12:
        bill = 5
        # print("You have to pay $5")
    elif age <= 15:
        bill = 7
        # print("You have to pay $7")
    else:
        bill = 9
        # print("You have to pay $9")

    wants_photo = input("Do you want to have a photo? Y or N")
    if not (age > 45 and age < 55) and wants_photo == "Y":
        bill += 3
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride this")
