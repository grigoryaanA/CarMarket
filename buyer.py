from person import Person
from car import Car


class Buyer(Person):
    """
    Buyer class inherits from Person and will have money,
    spent_money, and bought_cars attributes. The class will have methods for buying cars,
    returning cars, adding cars to the bought_cars list, and changing money.
    """

    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city)
        self._money = money
        self._spent_money = 0
        self._bought_cars = []

    @property
    def money(self):
        return self._money

    @property
    def spent_money(self):
        return self._spent_money

    @money.setter
    def money(self, value):
        if type(value) is int:
            self._money = value
        else:
            print("Money has to be type of int! ")

    @spent_money.setter
    def spent_money(self, value):
        if type(value) is int:
            self._spent_money = value
        else:
            print("Money has to ve type of int! ")

    def set_money(self, money):
        self.money = money

    def buy(self, car: Car):
        price = car.price + (car.price * car.discount)
        if self.money < price:
            print("You don have enaught money! ")
            return
        else:
            self.money -= price
            self.spent_money += price
            self._bought_cars.append(car)
            car.buyer = self

    def return_car(self, car: Car):
        if car in self._bought_cars:
            self.money += car.price
            self.spent_money -= car.price
            self._bought_cars.remove(car)
        else:
            print(f'{self.name} dont have a {car.model}! ')

    def print_my_cars(self):
        for car in self._bought_cars:
            print(f'{car.model} with price {car.price} and id {car.uid} from {car.seller.name} seller')
