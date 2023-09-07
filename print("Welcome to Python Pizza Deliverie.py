print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_s = 15
pizza_m = 20
pizza_l = 25

if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        pizza_s = 18
    elif add_pepperoni == "Y" and extra_cheese == "N":
        pizza_s = 17
    elif add_pepperoni == "N" and extra_cheese == "Y":
        pizza_s = 16
    else:
        # Neither pepperoni nor extra cheese is selected
        pizza_s = 15
    print(f"Your final bill is: ${pizza_s}.")

# You can extend this pattern for M and L sizes as well
