from store import CarMarket
from car import Car

market = CarMarket()
date = {
    "year": 2022,
    "moth": 1,
    "day": 1,
}


def update_date():
    if date["day"] <= 30:
        date["day"] += 1
    elif date["day"] == 30:
        date["day"] = 1
        if date["moth"] < 12:
            date["moth"] += 1
        else:
            date["moth"] = 1
            date["year"] += 1


market.load_data()
while True:
    market.get_data()
    # display menu options
    print("1. Add a car to the market")
    print("2. Add a buyer to the market")
    print("3. Add a seller to the market")
    print("4. Buy a car")
    print("5. Return a car")
    print("6. Get car discount")
    print("7. Get transactions")
    print("8. Exit\n")

    choose = int(input("Enter option: "))

    if choose == 1:
        model = input("Enter model: ")
        uid = int(input("Enter car id: "))
        price = int(input("Enter car price: "))
        discount = int(input("Enter discount: "))
        seller_name = input("Enter seller name: ")

        for seller in market.sellers:
            if seller.name == seller_name:
                car = Car(model, uid, price, seller, discount)
                market.add_car(car)
                print(seller.car_park)

    if choose == 2:
        loc_name = input("Enter buyer name: ")
        loc_surname = input("Enter buyer surname: ")
        loc_city = input("Enter buyer city: ")
        loc_money = int(input("Enter buyer money: "))
        market.add_buyer(loc_name, loc_surname, loc_city, loc_money)

    if choose == 3:
        loc_name = input("Enter seller name: ")
        loc_surname = input("Enter seller surname: ")
        loc_city = input("Enter seller city: ")
        loc_money = int(input("Enter seller money: "))
        market.add_seller(loc_name, loc_surname, loc_city, loc_money)

    if choose == 4:
        car_id = int(input("Enter car's id: "))
        buyer_name = input("Enter buyers name: ")
        buyer = None
        car = None

        for buyer_loc in market.buyers:
            if buyer_loc.name == buyer_name:
                buyer = buyer_loc
                break
        if buyer is None:
            print("No such buyer! ")

        for car_loc in market.car_park:
            if car_loc.id == car_id:
                car = car_loc
                break
        if car is None:
            print("No such car! ")

        if buyer is not None and car is not None:
            market.sell(car, buyer, date)

    if choose == 5:
        car_id = int(input("Enter car's id: "))
        car = None
        for car_loc in market.car_park:
            if car_loc.id == car_id:
                car = car_loc
                break;
        if car is None:
            print("No such car!")
        market.return_car(car, date)

    if choose == 6:
        car_id = int(input("Enter car's id: "))
        car = None
        for car_loc in market.car_park:
            if car_loc.id == car_id:
                car = car_loc
        market.get_car_available_discount(car)

    if choose == 7:
        for transaction in market.transactions:
            print(transaction)

    if choose == 8:
        break

    update_date()
