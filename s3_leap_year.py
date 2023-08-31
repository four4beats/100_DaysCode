# 🚨 Don't change the code below 👇
year = int(input("Is it a Leap Year? Enter a year to find out. "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
