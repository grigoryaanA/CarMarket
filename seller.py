"""
Seller will have car_park, money, and sold_cars attributes. car_park will contain the cars that the Seller has to sell,
 that list will be taken from CarMarket's get_seller_available_cars.
The Seller class should have the following methods:
sell - will sell the car. It will be a public method
change_money - will increase/decrease the amount. It will be a private method
return_car - will accept the return car. Here, the seller's amount should be reduced,
 the buyer's amount should be removed, and the status of the car in CarMarket should be changed
 (info about the return should be written).
 It will be a public method
get_available_cars - from CarMarket (get_seller_available_cars) will take the list of available cars of a particular
Seller.
 It will be a protected method
check_discount - will check if there is a discount for the buyer's car or not. It will be a protected method
add_sold_car - will add the sold car to Seller's sold_cars. Car model, buyer's name/surname/city, month, and date of
transaction should be specified in the following format: "year-month-day"
"""
from person import Person
from car import Car


class Seller(Person):

    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city)
        self._money = money
        self._car_park = []
        self._sold_cars = []
        self._discounts = {}

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money += value

    @property
    def sold_cars(self):
        return self._sold_cars

    @property
    def car_park(self):
        return self._car_park

    @property
    def discounts(self):
        return self._discounts

    def add_discounts(self, id, disc):
        for car in self.car_park:
            if id == car.id:
                self.discounts[id] = disc

    def _change_money(self, value):
        self.money += value

    def sell(self, car: Car):
        if car in self.car_park:
            if car.id in self.discounts:
                car.price -= self.discounts[car.id]
            self.money += car.price
            self.car_park.remove(car)
            self.sold_cars.append(car)

    def return_car(self, car: Car):
        for prod in self.sold_cars:
            if car.id == prod.id:
                self.sold_cars.remove(car)
                self.car_park.append(car)
                self._change_money(-car.price)

    def check_discount(self, car: Car):
        if car.id in self.discounts:
            return self.discounts[car.id]