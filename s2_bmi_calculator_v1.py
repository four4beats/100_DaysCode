# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# This is my attempt, which was accepted. Note: the BMI is converted to integer.
ht = float(height)
wt = float(weight)
print(int(wt / (ht**2)))

# Here is the solution Angela used to get the same result.
# bmi = int(weight) / float(height) ** 2
# bmi_as_integer = int(bmi)
# print(bmi_as_integer)
