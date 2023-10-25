# Which year do you want to check?
year = int(input("Pls enter the year"))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
temp = int(year/100)
if(year % 100 == 0):
    if (temp % 4 == 0):
        print("Leap year.")
elif(year % 4 == 0):
    print("Leap year")
else:
    print("Not leap year")
