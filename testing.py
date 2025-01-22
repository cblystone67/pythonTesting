#This program says hello and asks my name and age and tells me how old I'll be next year.

print("Hello World")
print("What is your name: ")
name = input()
print(f"Hello {name}")
print("How old are you: ")
age = int(input())
print(f"You will be {age + 1} years old in a year.")
nameLength = len(name)
print(f"Your name has {nameLength} letters in it.")
