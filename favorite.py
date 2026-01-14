#favorite.py - Git Homework Assignment
print("Hello from git-hw-20250449!")
print("This is my Python program for Assignment 3")

#My favorite number (using my university ID)
favorite_number = 20250449
print(f"My favorite number is: {favorite_number}")

#Simple calculation
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    sum_result = num + favorite_number
    print(f"{num} + {favorite_number} = {sum_result}")
except:
    print("Please enter a valid number!")

print("Program complete!")
