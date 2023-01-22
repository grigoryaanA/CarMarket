"""
Buyer will have money, spent_money, and bought_cars attributes. You will pass an arbitrary value to
Buyer money at the time of creating the Buyer object, and spent_money
should have an initial value of 0 (this attribute will show the amount spent by the buyer).
The Buyer class must have the following methods:

buy - will buy a car from the seller. It will be a public method
return_carr - will return the car (all updates resulting from it must be done). It will be a public method
change_money - will increase/decrease the amount. It will be a private method
add_bought_cars - will add the bought car to bought_cars. The car model, seller's name/surname/city,
 month, and date of the transaction must be specified in the following format: "year-month-day".
print_my_cars - will show the buyer's purchased cars. It will be a public method

"""
from person import Person
from car import Car


class Buyer(Person):

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

    @property
    def bought_cars(self):
        return self._bought_cars

    @money.setter
    def money(self, value):
        self._money = value

    @spent_money.setter
    def spent_money(self, value):
        self._spent_money = value

    def buy(self, car: Car):
        if self.money >= car.price:
            self.money -= car.price
            self.bought_cars.append(car)
        else:
            print("No souch money! ")

    def return_car(self, returnable: Car):
        for car in self.bought_cars:
            if car.id == returnable.id:
                self.bought_cars.remove(car)
                self.spent_money -= car.price
                self.money += car.price
            else:
                print("Theres not such a car! ")

    def print_my_cars(self):
        for car in self.bought_cars:
            print(f'{car.name} with price {car.price} and id {car.id}')
