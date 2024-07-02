
def greet(name):
    print("Hello " + name + "!")


def add(a, b):
    return a + b


result = add(3, 4)

print(result)

ingredient1 = "Mandrake Root"
ingredient2 = "Unicorn Hair"
ingredient3 = "Dragon Scale"

potion = [ingredient1, ingredient2, ingredient3]

""" print(potion)

herbs = []
for i in range(10):
    herbs.append("Magical Herb")
print(herbs)
 """

# herbs = []
# i = 0
# while i < 10:
#     herbs.append("Magical Herb")
#     i += 1
# print(herbs)

number = 5
if number > 0 and number % 2 == 0:
    print("Take the right path")
elif number > 0 and number % 2 != 0:
    print("Take the upper path")
elif number == 0:
    print("Stay where you are.")
else:
    print("Take the left path")

greet("Adventurer")
