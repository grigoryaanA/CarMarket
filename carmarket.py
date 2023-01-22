"""
The CarMarket class must have the following methods:
add_car - adds a new car to the car list.
remove_car - will delete car/cars. It will be a private method set_discount
- will set a discount on the car/cars. It will be a protected method
get_sold_car_history - will return cars sold by a specific seller. The price of each car,
the day/month/date of the transaction, the buyer's name/surname/city,
if the car had a discount, then also the discount, if the car was returned, then also information about the return.
It will be a private method return_car - a return of the car by the buyer, in this case, in the payment history,
for the returned car, it is written that it was returned and the reason for the return. It will be a private method
get_seller_available_cars-will return the cars currently available for sale at the Seller. It will be a protected method
get_car_available_discount - will return the available discount for the car.
"""
from person import Person
from car import Car
from seller import Seller
from buyer import Buyer


class CarMarket:
    def __init__(self):
        self._sellers = []
        self._buyers = []
        self._cars = []
        self._history = []

    def get_seller(self, name):
        for i in self._sellers:
            if i.name == name:
                return i

    def get_buyer(self, name):
        for i in self._buyers:
            if i.name == name:
                return i

    @property
    def sellers(self):
        return self._sellers

    @property
    def buyers(self):
        return self._buyers

    @property
    def cars(self):
        return self._cars

    @property
    def history(self):
        return self._history

    def add_car(self, model, id, price):
        for i in self.cars:
            if id == i.id:
                print("Car exists! ")
            else:
                self.cars.append(Car(model, id, price))

    def add_seller(self, name, surname, city, money):
        self.sellers.append(Seller(name, surname, city, money))

    def add_buyer(self, name, surname, city, money):
        self.buyers.append(Buyer(name, surname, city, money))

    def sell(self, car, seller, buyer):
        if car in self.cars:
            if seller in self.sellers:
                if buyer in self.buyers:
                    if car in seller.car_park:
                        seller.sell(car)
                        buyer.buy(car)
                        self.history.append([car, buyer, seller])
                    print("Seller can't sell this car ")
                print("Buyer not found! ")
            print("Seller not found! ")
        print("Theres no such a car! ")

    def bind_car_to_seller(self, car, seller):
        seller.car_park.append(car)

    def set_discount(self, car, discount):
        if car in self.cars:
            for selpers in self.sellers:
                if car in selpers.car_park:
                    selpers.discount[car.id] = discount

    def return_car(self, car, buyer, seller):
        if seller in self.sellers:
            if buyer in self.buyers:
                if car in buyer.bought_cars:
                    if car in seller.sold_cars:
                        buyer.return_car(car)
                        seller.return_car(car)
                    print("This seller is incorect! ")
                print("This buyer has not such a car! ")
            print("Buyer not found! ")
        print("Seller not found! ")

    def get_history(self):
        for i in self.history:
            print(f'{i[0]} buyer: {i[1]} seller: {i[2]} ')

    def get_seller_available_cars(self, name):
        for seller in self.sellers:
            if name == seller.name:
                print(name + " available cars are")
            for car in seller.car_park:
                print(car.model + " with price " + car.price)
        else:
            print("Seller not found! ")

    def get_car_available_discount(self, car):
        print(f'for {car.name} discounts are')
        for i in self.sellers:
            if i.discounts[car.id] != 0:
               print(f'{i.name: } sellers discount for this model is {i.discounts[car.id]}')

