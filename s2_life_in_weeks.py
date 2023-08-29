# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# First, figure out how many total days, weeks, months a 90 year old has.
DAYS_90_YRS = 90 * 365
WEEKS_90_YRS = 90 * 52
MONTHS_90_YRS = 90 * 12
# I used UPPER CASE for these variables because Pylint considered them Constants.
# I can also use the following code to turn off Pylint from checking for naming conventions:
# pylint: disable=C0103

# Then, calculate how many days, weeks, months the user has lived.
age_in_days = int(age) * 365
age_in_weeks = int(age) * 52
age_in_months = int(age) * 12

# Finally, subtract the 90 year old's totals vs the user's d/w/m.
days_left = DAYS_90_YRS - age_in_days
weeks_left = WEEKS_90_YRS - age_in_weeks
months_left = MONTHS_90_YRS - age_in_months

# Print the answer.
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
