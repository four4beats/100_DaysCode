print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Write your code below this line 👇
combined_string = name1 + name2
lower_case_string = combined_string.lower()

# I didn't get this part, but it counts the individual letters
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# without wrapping in the int, an error will occur below with the comparison operators "<" and "">""
# the str function with the + concatenates the string values of 'true' and 'love'
# so if true = 6 and love = 7 the love_score would be 67.
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")


# ChatGPT gave me the wrong answer, though I didn't really understand this.
# name1 = name1.lower()
# name2 = name2.lower()

# # Define letters to count
# letters_to_count1 = ["t", "r", "u", "e"]

# letters_to_count2 = ["l", "o", "v", "e"]

# # Count occurrences of each letter in name1
# counts1 = {letter: name1.count(letter) for letter in letters_to_count1}

# # Count occurrences of each letter in name2
# counts2 = {letter: name2.count(letter) for letter in letters_to_count2}

# # Calculate the sums for each name
# sum1 = sum(counts1.values())
# sum2 = sum(counts2.values())

# # Convert the sums to strings and concatenate them
# total_count = int(str(sum1) + str(sum2))

# if 10 >= total_count or total_count >= 90:
#     print(f"Your score is {total_count}, you go together like coke and mentos.")

# elif 40 <= total_count <= 50:
#     print(f"Your score is {total_count}, you are alright together.")

# else:
#     print(f"Your score is {total_count}.")
