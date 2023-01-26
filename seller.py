from person import Person
from car import Car


class Seller(Person):
    """
    The Seller class
        will inherit from Person and will have car_park,
        money, and sold_cars attributes. The class will have methods for selling cars, returning cars,
        adding cars to the sold_cars list, getting available cars, checking discounts, and changing money.
    """

    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city)
        self._money = money
        self._car_park = []
        self._sold_cars = []

    @property
    def money(self):
        return self._money

    @property
    def sold_cars(self):
        return self._sold_cars

    @property
    def car_park(self):
        return self._car_park

    @money.setter
    def money(self, value):
        if type(value) is int:
            self._money = value
        else:
            print("Money has to be type of int! ")

    def add_car(self, car):
        if car not in self.car_park:
            self._car_park.append(car)

    def remove_car(self, car):
        if car in self.car_park:
            self._car_park.remove(car)

    def sell(self, car: Car):
        self.money += car.price - (car.discount * car.price)
        self.remove_car(car)
        self._sold_cars.append(car)

    def return_car(self, car):
        if car in self.sold_cars:
            self.money -= car.price
            self.add_car(car)
            self.sold_cars.remove(car)
        else:
            print(f'{car.model} was not sold by {self.name}! ')

    def get_available_cars(self):
        for car in self.car_park:
            print(f"{car.model} with id {car.uid} and price {car.price}")

    def check_discount(self, car):
        if car in self.car_park:
            return car.discount
        else:
            print(f'{car.model} is not in {self.name} car park! ')
