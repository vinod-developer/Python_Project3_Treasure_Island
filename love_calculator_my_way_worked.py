print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
count = 0
count2 = 0
checking_word = "true"
checking_word_2 = "love"
names_combine = name1 +name2
for letter in names_combine:
    if letter in checking_word:
        count+=1
print(f"count for true name1 is {count}")
for letter in names_combine:
    if letter in checking_word_2:
        count2+=1
print(f"count for love name1 is {count}")
count1_in_string = str(count)
count2_in_string = str(count2)
combine = count1_in_string+count2_in_string
combine_in_int = int(combine)
if combine_in_int < 10 or combine_in_int > 90:
    print(f"Your score is {combine_in_int}, you go together like coke and mentos.")
elif combine_in_int > 40 or combine_in_int < 50:
    print(f"Your score is {combine_in_int}, you are alright together.")
else:
    print(f"Your score is {combine_in_int}")


