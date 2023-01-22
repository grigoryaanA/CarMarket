"""We will have a Person superclass. 2 classes will inherit from Person: Buyer and Seller classes.
Person will have a name, surname, and city attributes."""


class Person:

    def __init__(self, name, surname, city):
        self._name = name
        self._surname = surname
        self._city = city

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def city(self):
        return self._city
