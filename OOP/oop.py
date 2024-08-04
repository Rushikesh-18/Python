class Car:
    def __init__(self,ubrand,umodel):
        self.brand= ubrand
        self.model= umodel
    
    def fullname(self):
        return f"{self.brand}={self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):

        super().__init__(brand,model)
        self.battery_size=battery_size




my_tesla = ElectricCar("Tesla","5","90KWh")

print(my_tesla.fullname(),my_tesla.battery_size)
my_car=Car("MorissGaarage","Hector")
print(my_car.brand)

my_car2=Car("Mahindra","marazzo")

print(my_car2.fullname())