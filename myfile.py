
def addThree(val):
    return val * 3


print(addThree(8))


class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')


my_dog = Dog('Rover')
anotherDog = Dog('Fluffy')

my_dog.speak()
anotherDog.speak()


def factorial(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    print("Factors of {} = {}")
