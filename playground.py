def add(*arg):
    result = 0
    for i in arg:
        result += i
    return result


print(add(1, 5, 4, 3, 8, 9, 10, 50))


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)


calculate(add=3, muliply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


car = Car(make="BMW", model="X5")

print(car.model)
