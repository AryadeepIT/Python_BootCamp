def calculate(**kwargs):
    print(kwargs)  # returns dictionary 'dict' type
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"])   # 3


calculate(add=3, multiply=5)


def calculate1(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate1(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R", color="blue", seats=4)
print(my_car.seats)
