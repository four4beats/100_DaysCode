# DON'T CHANGE THE OPENING INPUTS
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# CONSTANTS
PIZZA_S = 15
PIZZA_M = 20
PIZZA_L = 25
if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        PIZZA_S = 18

    elif add_pepperoni == "Y" and extra_cheese == "N":
        PIZZA_S = 17

    elif add_pepperoni == "N" and extra_cheese == "Y":
        PIZZA_S = 16

    else:
        # Neither pepperoni nor extra cheese is selected
        PIZZA_S = 15
    print(f"Your final bill is: ${PIZZA_S}.")

if size == "M":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        PIZZA_M = 24

    elif add_pepperoni == "Y" and extra_cheese == "N":
        PIZZA_M = 23

    elif add_pepperoni == "N" and extra_cheese == "Y":
        PIZZA_M = 21

    else:
        # Neither pepperoni nor extra cheese is selected
        PIZZA_M = 20
    print(f"Your final bill is: ${PIZZA_M}.")

if size == "L":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        PIZZA_L = 29

    elif add_pepperoni == "Y" and extra_cheese == "N":
        PIZZA_L = 28

    elif add_pepperoni == "N" and extra_cheese == "Y":
        PIZZA_L = 26

    else:
        # Neither pepperoni nor extra cheese is selected
        PIZZA_L = 25
    print(f"Your final bill is: ${PIZZA_L}.")

# I WASN'T GETTING THE PRINT STATEMENT TO APPEAR WHEN BOTH OPTIONS WERE "N".
# I HAD TO MOVE THE INDENTATION TO THE SAME LEVEL AS THE IF STATEMENTS FOR IT TO WORK.
# PRINT WAS ORIGINALLY ON THE SAME INDENTATION AS THE PIZZA PRICE.

# Here is Angela's solution code:
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")

# HERE IS CHATGPT'S VERSION OF THIS CODE
# REMOVING THE REPEATED 'IF/ELIF/ELSE' STATEMENTS
# IN FAVOR OF USING A DICTIONARY TO LOOK UP THE COST

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Base prices for each pizza size
base_prices = {"S": 15, "M": 20, "L": 25}

# Additional costs for pepperoni and extra cheese
pepperoni_prices = {"S": 2, "M": 3, "L": 3}
cheese_price = 1

# Calculate final price
final_price = base_prices.get(size, 0)

if add_pepperoni == "Y":
    final_price += pepperoni_prices.get(size, 0)

if extra_cheese == "Y":
    final_price += cheese_price

print(f"Your final bill is: ${final_price}.")
