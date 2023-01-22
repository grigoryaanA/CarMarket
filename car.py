class Car:

    def __init__(self, model, price, id):
        self._model = model
        self._price = price
        self._id = id

    @property
    def model(self):
        return self._model

    @property
    def price(self):
        return self._price

    @property
    def id(self):
        return self._id

    @price.setter
    def price(self, value):
        self._price = value
