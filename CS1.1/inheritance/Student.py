from Person import Person


class Student(Person):

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
        self.courses = []

    def introduce_self(self):
        """This method prints out the name and age attributes"""

        print(
            f"My name is {self._name} and my age is {self._age}. I am a {self.year}")

    def get_courses(self):
        print(f"{self._name} is taking CS1.1, Web1.1, SPD1.2, and S&L")
