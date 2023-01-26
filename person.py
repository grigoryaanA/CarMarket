class Person:
    """
    super class for buyer and seller classes
    """

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
