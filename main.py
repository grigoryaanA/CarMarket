from carmarket import CarMarket

market = CarMarket()


while True:
    print("CarMarket:")
    print("To add seller enter Seller: ")
    print("To add buyer enter Buyer: ")
    print("To add car enter Car: ")
    print("To sell car enter S: ")
    print("To return car enter R: ")
    print("To get seller available cars SC:")
    print("To get market history enter H: ")
    print("To get cars available discount: CD")
    print("To set discount for a car: SD")
    print("To bind car to a seller: B\n\n")

    choose = input("Enter your option: ")

    if choose == "Seller":
        name = input("Enter sellers name: ")
        surname = input("Enter sellers surname: ")
        city = input("Enter sellers city: ")
        money = int(input("Enter sellers money: "))
        market.add_seller(name, surname, city, money)

    if choose == "Buyer":
        name = input("Enter buyers name: ")
        surname = input("Enter buyers surname: ")
        city = input("Enter buyers city: ")
        money = int(input("Enter buyer money: "))
        market.add_buyer(name, surname, city, money)

    if choose == "Car":
        model = input("Enters cars model: ")
        uid = int(input("Enter cars id: "))
        price = int((input("Enter cars price: ")))
        market.add_car(model, uid, price)

    if choose == "S":
        seller_n = input("Enter seller name: ")
        buyer_n = input("Enter buyer name: ")
        car_id = input("Enter car id: ")
        sel_car , buy, sel = None, None, None
        for seller in market.sellers:
            if seller_n == seller.name:
                sel = seller
            else:
                print("No seller found! ")
        for buyer in market.buyers:
            if buyer_n == buyer.name:
                buy = buyer
            else:
                print("No buyer found! ")
        for car in market.cars:
            if car_id == car.id:
                sel_car = car
            else:
                print("No car found! ")

        market.sell(sel_car, sel, buy)

    if choose == "R":
        seller_n = input("Enter seller name: ")
        buyer_n = input("Enter buyer name: ")
        car_id = input("Enter car id: ")
        sel_car, buy, sel = None, None, None
        for seller in market.sellers:
            if seller_n == seller.name:
                sel = seller
            else:
                print("No seller found! ")
        for buyer in market.buyers:
            if buyer_n == buyer.name:
                buy = buyer
            else:
                print("No buyer found! ")
        for car in market.cars:
            if car_id == car.id:
                sel_car = car
            else:
                print("No car found! ")

        market.return_car(sel_car, buy, sel)

    if choose == "SC":
        name = input("Enter sellers name: ")
        market.get_seller_available_cars(name)

    if choose == "H":
        market.get_history()

    if choose == "CD":
        car_id = int(input("Enter cars id: "))
        check_car = None
        for car in market.cars:
            if car_id == car.id:
                check_car = car
        market.get_car_available_discount(check_car)

    if choose == "SD":
        discount = int(input("Enter discount: "))
        car_id = int(input("Enter cars id: "))
        check_car = None
        for car in market.cars:
            if car_id == car.id:
                check_car = car
        market.set_discount(check_car,discount)

    if choose == "B":
        seller_n = input("Enter seller name: ")
        car_id = input("Enter car id: ")
        sel_car, sel = None, None
        for seller in market.sellers:
            if seller_n == seller.name:
                sel = seller
            else:
                print("No seller found! ")
        for car in market.cars:
            if car_id == car.id:
                sel_car = car
            else:
                print("No car found! ")
        market.bind_car_to_seller(sel_car, sel)