# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# The assignment wanted the BMI rounded to nearest whole number.
user_bmi = round(weight / (height**2))

# Used the f-string to concatenate the first print statement.
# The end="" statement allowed the if/else print statement to be on the same line in the final output.
message = f"Your BMI is {user_bmi}, "
print(message, end="")

if user_bmi <= 18.5:
    print("you are underweight.")
elif user_bmi <= 25:
    print("you have a normal weight.")
elif user_bmi <= 30:
    print("you are slightly overweight.")
elif user_bmi <= 35:
    print("you are obese.")

else:
    print("you are clinicly obese.")

# Angela's tutorial example just moved the whole print statement into the if/else, so she didn't use the end="" statement.
# Example:
# if bmi < 25
# print(f"Your bmi is {user_bmi}, you have a normal weight.")
