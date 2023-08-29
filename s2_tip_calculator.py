# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Get the amount of people
subtotal = input("Welcome to the tip calculator. How much was your bill? $")
# Convert to integer
subtotal = float(subtotal)

# Get the tip amount
# Obtain the tip percentage or amount from the user
tip = input(
    "How much would you like to add for the tip 15%, 18%, 20% (you may also add a custom amount)? "
)
# Remove any percent signs
tip = tip.replace("%", "")

# Convert it to float
try:
    tip_convert = float(tip)
except ValueError:
    print("Invalid input for tip. Please enter a number.")
    exit()

# The number of people splitting
party = input("How many people are splitting this bill? ")

# Convert to integer
party = int(party)

# Calculate the total
tipped_amount = tip_convert / 100 + 1
total = subtotal * tipped_amount
split_total = (subtotal / party) * tipped_amount

# Print the final amounts
print("The total bill with tip is: $", round(total, 2))
print("The split amount is: $", round(split_total, 2))

# The code above was my attempt.

# ChatGPT assisted code is below. I asked it about the try: control structure and exceptions. # # Obtain the subtotal from the user
# subtotal = input("Welcome to the tip calculator. How much was your bill? ")
# # Convert it to float
# try:
#     subtotal = float(subtotal)
# exceet ValueEr#or:
#    eice# # # Convert it to float
# try:
#     tip_convert = float(tip)
# except ValueError:
#     print("Invalid input for tip. Please enter a number.")
#     exit()

# # Obtain the number of people from the user
# party = input("How many people are splitting this bill? ")
# # Convert it to integer
# try:
#     party = int(party)
# except ValueError:
#     print("Invalid input for the number of people. Please enter a number.")
#     exit()

# # Check if party is zero and set it to 1 if so
# if party == 0:
#     print("The number of people splitting the bill cannot be zero. Setting it to 1.")
#     party = 1

# # Calculate the total amount
# tipped_amount = tip_convert / 100 + 1
# total = (subtotal / party) * tipped_amount

# print("The amount everyone should pay is:", round(total, 2))
