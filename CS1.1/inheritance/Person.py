# Person Class
class Person:
    """This class represents a person"""

    def __init__(self, name, age):
        """This method initializes the Person class with name and age attributes protected"""

        self._name = name
        self._age = age

    def introduce_self(self):
        """This method prints out the name and age attributes"""

        print(f"My name is {self._name} and my age is {self._age}")
