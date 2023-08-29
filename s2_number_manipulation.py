# Division in Python will always result in a floating point number.
print(8/3)

# use the round() function to round the number into an integer.
print(round(8 / 3))

# the round() syntax can use a "," to define number of decimal places
print(round(8 / 3, 3))

# if the division is assigned a variable, it's possible to continue calculating the result
result = 4 / 2
result /= 2
print(result)

# When you have to manipulate a value based on its previous value use an (operator)= to get the new value.
score = 100
# user scores 10 points
score += 10
print(score)

# f-String converts different data types into a string. place "f" in front of the string and variables in curly braces {}
score = 100
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, and true or false, are you winning? {isWinning}.")

