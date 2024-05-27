from AbstractVehicle import AbstractVehicle


# first one is the file name and second abstracvehicle is class name
class Bike(AbstractVehicle):

    def display_details(self):
        print("Bike details:")
        print("color:", self.color)
        print("number of tyres:", self.num_tyres)
        print("gears:", self.gears)


class Car(AbstractVehicle):
    def display_details(self):
        print("car details:")
        print("color:", self.color)
        print("number of tyres:", self.num_tyres)
        print("gears:", self.gears)


class Scooty(AbstractVehicle):
    def display_details(self):
        print("scooty details:")
        print("color:", self.color)
        print("number of tyres:", self.num_tyres)
        print("gears:", self.gears)


class Bus(AbstractVehicle):
    def display_details(self):
        print("bus details:")
        print("color:", self.color)
        print("number of tyres:", self.num_tyres)
        print("gears:", self.gears)


class Auto(AbstractVehicle):
    def display_details(self):
        print("auto details:")
        print("color:", self.color)
        print("number of tyres:", self.num_tyres)
        print("gears:", self.gears)