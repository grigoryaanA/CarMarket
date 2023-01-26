import sqlite3
from seller import Seller
from buyer import Buyer
from car import Car


class CarMarket():
    """
    The CarMarket class
    will store the cars for sale and will have methods for adding new cars, removing cars,
    setting discounts, and returning cars.
    The class will also have a private method for getting the history of sold cars,
    and a protected method for getting the available cars for a specific seller.
    """

    def __init__(self):
        self.connection = sqlite3.connect("market.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars
            (
                model  TEXT,
                uid INTEGER,
                price INTEGER,
                discount INTEGER,
                seller TEXT,
                buyer TEXT
            )""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sellers
            (
                name TEXT,
                surname TEXT,
                city TEXT,
                money INTEGER
            )""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS buyers
            (
                name TEXT,
                surname TEXT,
                city TEXT,
                money INTEGER,
                spent_money INTEGER
            )
        """)
        self.buyers = []
        self.sellers = []
        self.car_park = []
        self.transactions = []

    def add_buyer(self, name, surname, city, money):
        self.buyers.append(Buyer(name, surname, city, money))
        self.cursor.execute("""
            INSERT INTO buyers 
            (name, surname, city, money, spent_money) VALUES (?, ?, ?, ?, ?)
        """, (name, surname, city, money, 0))
        self.connection.commit()

    def add_seller(self, name, surname, city, money):
        self.sellers.append(Seller(name, surname, city, money))
        self.cursor.execute("""
            INSERT INTO sellers 
            (name, surname, city, money) VALUES (?, ?, ?, ?)
        """, (name, surname, city, money))
        self.connection.commit()

    def add_car(self, car: Car):
        self.car_park.append(car)
        self.bind_cars_to_seller()
        self.cursor.execute("""
            INSERT INTO cars 
            (model, uid, price, discount, seller, buyer) VALUES (?, ?, ?, ?, ?, ?)
        """, (car.model, car.id, car.price, car.discount, car.seller.name, ""))
        self.connection.commit()

    def bind_cars_to_seller(self):
        for car in self.car_park:
            for seller in self.sellers:
                if car.seller == seller:
                    seller.add_car(car)

    def sell(self, car: Car, buyer: Buyer, date):
        buyer.buy(car)
        car.seller.sell(car)

        self.transactions.append({
            "car": car.model,
            "buyer": buyer.name + " " + buyer.surname + " " + buyer.city,
            "seller": car.seller.name + " " + car.seller.surname + " " + car.seller.city,
            "date": str(date["year"]) + "-" + str(date["moth"]) + "-" + str(date["day"]),
            "type": "buying"
        })

        self.cursor.execute("""
            UPDATE cars
            SET buyer = ?
            WHERE uid = ?
        """, (buyer.name, car.id))
        self.cursor.execute("""
            UPDATE buyers
            SET money = ?
            SET spent_money = ?
            WHERE name = ?
        """, (buyer.money, buyer.spent_money, buyer.name))
        self.cursor.execute("""
            UPDATE sellers
            SET money = ?
            WHERE name = ?
        """, (car.seller.money, car.seller.name))
        self.connection.commit()

    def return_car(self, car: Car, date):
        buyer = car.buyer
        car.buyer.return_car(car)
        car.seller.return_car(car)
        self.transactions.append({
            "car": car.model,
            "buyer": car.buyer.name + " " + car.buyer.surname + " " + car.buyer.city,
            "seller": car.seller.name + " " + car.seller.surname + " " + car.seller.city,
            "date": str(date["year"]) + "-" + str(date["moth"]) + "-" + str(date["day"]),
            "type": "return"
        })
        self.cursor.execute("""
            UPDATE cars 
            SET buyer = ? 
            WHERE id = ?
        """, ("", car.id))
        self.cursor.execute("""
            UPDATE sellers
            SET money = ?
            WHERE name = ?
        """, (car.seller.money, car.seller.name))
        self.cursor.execute("""
            UPDATE buyers
            SET money = ?
            WHERE name = ?
        """, (buyer.money, buyer.name))
        self.connection.commit()

    def get_seller_available_cars(self, seller: Seller):
        if seller in self.sellers:
            seller.get_available_cars()
        else:
            print(f"{seller.name} seller not found! ")

    def get_car_available_discount(self, car: Car):
        if car in self.car_park:
            print(f"{car.model}'s discount is {car.discount}")
        else:
            print(f"there is not {car.model} cars model in stores car park! ")

    def load_data(self):
        self.cursor.execute("SELECT * FROM cars")
        cars = self.cursor.fetchall()
        seller_obj = None
        for car in cars:
            model, uid, price, discount, seller, buyer = car
            for sell in self.sellers:
                if seller == sell.name:
                    seller_obj = sell
            self.car_park.append(Car(model, uid, price, seller_obj, discount))
        self.cursor.execute("SELECT * FROM sellers")
        sellers = self.cursor.fetchall()
        for seller in sellers:
            name, surname, city, money = seller
            self.sellers.append(Seller(name, surname, city, money))
        self.cursor.execute("SELECT * FROM buyers")
        buyers = self.cursor.fetchall()
        for buyer in buyers:
            name, surname, city, money, spent_money = buyer
            self.buyers.append(Buyer(name, surname, city, money))

    def get_data(self):
        self.cursor.execute("SELECT * FROM cars")
        cars = self.cursor.fetchall()
        print("Cars:")
        for car in cars:
            print(car)
        self.cursor.execute("SELECT * FROM sellers")
        sellers = self.cursor.fetchall()
        print("Sellers:")
        for seller in sellers:
            print(seller)
        self.cursor.execute("SELECT * FROM buyers")
        buyers = self.cursor.fetchall()
        print("Buyers:")
        for buyer in buyers:
            print(buyer)

    def clean_data(self):
        self.cursor.execute("DELETE FROM cars")
        self.cursor.execute("DELETE FROM buyers")
        self.cursor.execute("DELETE FROM sellers")
        self.connection.commit()
