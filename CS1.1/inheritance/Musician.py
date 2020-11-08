from Person import Person


class Musician(Person):
    def __init__(self, name, age, instruments):
        super().__init__(name, age)
        self.instruments = instruments
    # Create an __init__ that also has an instance attribute 'instruments', a list to store the instruments

    def get_instruments(self):
        print(self.instruments)
    # Overrides Introduce Self

    def introduce_self(self):
        print(
            f"My name is {self._name} and my age is {self._age} and I like to play { ', '.join(self.instruments) }")


joi = Musician("Joi", 25, ['flute', 'piccolo', 'piano'])
joi.get_instruments()
joi.introduce_self()
