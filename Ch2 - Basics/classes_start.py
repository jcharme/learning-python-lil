#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed
    
    def park(self):
        self.mode = "park"

    def reverse(self, speed):
        self.mode = "reverse"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype, type):
        super().__init__("Car")
        self.wheels = 4
        self.enginetype = enginetype
        self.type = type
        if (type == "convertible"):
            self.doors = 2
        else:
            self.doors = 4

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, self.type, "at", self.speed)
    
    def park(self):
        super().park()
        print("I parked my", self.enginetype, self.type)

    def reverse(self, speed):
        super().reverse(speed)
        print("Reversing my", self.enginetype, self.type, "at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

    def park(self):
        super().park()
        print("I parked my", self.enginetype, "motorcycle")

    def reverse(self, speed):
        super().reverse(speed)
        print("Reversing my", self.enginetype, "motorcycle at", self.speed)


car1 = Car("gas", "sedan")
car2 = Car("electric", "convertible")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype, car1.doors)
print(car2.doors)

car1.drive(30)
car2.park()
mc1.reverse(50)