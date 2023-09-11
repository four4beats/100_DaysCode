print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Get off the ship, your mission is to find the treasure.")
print("You have until sunrise to bring back the treasure...or off with ye head!")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
q1 = input(
    "Look for treasure or attempt a getaway by jumping overboard? Type 'look' or 'jump'. "
).lower()

if q1 == "look":
    print("Smart choice. These are shark infested waters.")
else:
    print(
        "Argh! You jumped in directly into a shark infested waters. You're a goner. Game over."
    )
    exit()

q2 = input(
    "You've been walking a few miles and arrive at a crossroad. There's a cave on your left but the path continues to the right. Type 'left' or 'right'. "
).lower()

if q2 == "left":
    print("Proceed with caution.")
    q2a = input(
        "It gets super dark after a 50-feet. Keep going in or turn back? Type 'in' or 'back'. "
    ).lower()

    if q2a == "in":
        print(
            "You fell into a deep, dark hole and broke your leg. Sorry mate. Game over."
        )
        exit()

    elif q2a == "back":
        print("The dark gives you the heebeejeebees. Best to stay in the light.")

else:
    print(
        "Who knows what dangers are lurking in there. Let's keep going down this path."
    )

q3 = input(
    "You realize you have no water or food. It's very hot. Look for treasure or water? Type 'treasure' or 'water'. "
).lower()

if q3 == "treasure":
    print("Let's keep looking. It's got to be close.")

else:
    print("Better look for water or you might die before finding the treasure.")

q4 = input(
    "The path leads to the base of a mountain. Hike up or head towards the jungle? Type 'hike' or 'jungle'? "
).lower()

if q4 == "hike":
    print("You hear the sound of rushing water. Maybe there's a waterfall?")

else:
    print(
        "You head towards the jungle and feel relief when you hear the sound of water."
    )
    print(
        "The relief turns into terror when a herd of wild pigs start chasing you and eat you alive. What a horrible way to die. Game over."
    )
    exit()

print("You continue hiking up the trail and head towards the sound of water.")
print("Could that be? It's a waterfall! You run towards it.")
print("You drink the glorious refereshing water when a bright glint catches your eye.")
print("Behind the waterfall you find the treasure and a wooden raft!")

q5 = input(
    "Do you walk back to the ship with the treasure or grab what you can and try to escape on the raft? Type 'ship' or 'raft'. "
).lower()

if q5 == "ship":
    print("You drag the heavy treasure all the way back to the ship.")
    print("The pirate captain laughs with joy when he sees you.")
    print('The moment you board the ship, the captain yells, "OFF WITH HIS HEAD!"')
    q5a = input("Fight and run or just run? Type 'fight' or 'run' ")
    if q5a == "fight":
        print(
            "Turns out the pirates don't know how to fight. You overtake the captain, take his sword, and kill him in front of the other pirates. You win."
        )
        print(
            "You go find Emma Patrick and offer her the treasure then she becomes supa dupa rich and is the richest person in the world."
        )

    else:
        print(
            'You take off running but trip over a plank. Turns out the black-bearded gold toothed captain was your friend Kate Patrick. She giggles then shouts out "OH MY DAYS" and tortures you for the rest of your life. Game over.'
        )
else:
    print("You get going down the river on the raft with pockets full of gold.")
    print("You notice the raft isn't holding together very well.")
    print("The raft begins to come apart and you fall into the water.")
    print(
        "All the gold in your pockets weighs you down. As you try to swim to a shore, a crocodile slides into the river."
    )
    print(
        "You try to swim the other way but the crocodile bites your legs and pulls you under the water and eats your leg before you begin to drown."
    )
    print("The end.")
    exit()
