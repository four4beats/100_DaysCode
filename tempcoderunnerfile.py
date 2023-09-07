# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
pizza_s = 15
pizza_m = 20
pizza_l = 25
if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        pizza_s = 18
        print(f"Your final bill is: ${pizza_s}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        pizza_s = 17
        print(f"Your final bill is: ${pizza_s}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        pizza_s = 16
        print(f"Your final bill is: ${pizza_s}.")
else:
    pizza_s = 15
    print(f"Your final bill is: ${pizza_s}.")