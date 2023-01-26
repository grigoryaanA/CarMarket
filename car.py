class Car:
    """
    Car class for CarMarket
    """
    def __init__(self, model, uid, price, seller, discount):
        self._model = model
        self._id = uid
        self._price = price
        self._seller = seller
        self._discount = discount
        self._buyer = None

    @property
    def model(self):
        return self._model

    @property
    def id(self):
        return self._id

    @property
    def price(self):
        return self._price

    @property
    def seller(self):
        return self._seller

    @property
    def discount(self):
        return self._discount

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        self._buyer = value

    @discount.setter
    def discount(self, value):
        if type(value) == int:
            self._discount = value
        else:
            print("Discount must be an integer! ")
