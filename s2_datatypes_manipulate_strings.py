# #Data Types

# #String

# print("Hello"[4])

# #Integer are whole numbers

# print(123 + 345)

# #Float numbers have decimals

# 3.14159

# #Boolean - true or false
# True
# False

# #Strings can't concatenate with integers or other data types

# num_char = len(input("What is your name?"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

# a = str(123)
# print(type(a))

# 21 - Coding Exercise - Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num1 = two_digit_number[0]
num2 = two_digit_number[1]
answer = int(num1) + int(num2)
print(answer)