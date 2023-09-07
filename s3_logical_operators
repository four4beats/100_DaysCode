print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# The indentation under the 'if' and 'else' statement is important.
# if height >= 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry, you have to be taller to go on the ride.")

# Nested if/else statements and elif

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets price is $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets price is $7.")
    elif 45 <= age <= 55:
        bill = 0
        print("Congrats old timer, you ride for free!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like to add a printed photo for $3.00? y or n. ")
    if wants_photo == "y":
        bill += 3
    print(f"Thank you. Your final bill is ${bill}.")

else:
    print("Sorry, you have to be taller to go on the ride.")
