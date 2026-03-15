# Week 1 Project: Personal Introduction Program
# This program asks the user for personal details
# and displays a friendly welcome message.

print("Welcome to the Personal Introduction Program!")
print("Please answer the following questions:\n")

# Taking user input
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city are you from? ")
hobby = input("What is your favorite hobby? ")

# Displaying a friendly message
print("\n" + "=" * 50)
print(f"Hello, {name}!")
print(f"You are {age} years old and you are from {city}.")
print(f"It's awesome that you enjoy {hobby}!")
print("Nice to meet you! Have a wonderful day!")
print("=" * 50)