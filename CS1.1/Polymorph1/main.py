class Car(object):

    def __init__(self, color, make, speed_limit):
        self.color = color
        self.make = make
        self.speed_limit = speed_limit

    def accelerate(self, speed):
        if speed <= self.speed_limit:
            return "now driving at " + str(speed) + " MPH"
        else:
            return "that is too fast for me!"

    def park(self, parking_spot_type):
        if parking_spot_type == "parallel":
            return "parallel parking...good luck!"
        else:
            return "parking car!"


class Tesla(Car):
    def __init__(self, color, make, speed_limit, battery_level):
        super().__init__(color, make, speed_limit)
        self.battery_level = battery_level


my_car = Car("blue", "VW", 120)
print(my_car.color)
# print(my_car.battery_level)
your_car = Tesla("black", "Tesla", 160, 100)
print(your_car.color)
print(your_car.battery_level)

print(my_car.accelerate(140))

print(your_car.accelerate(140))
