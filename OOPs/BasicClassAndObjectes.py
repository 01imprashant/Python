class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+"!"    

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Disel"
    
    @staticmethod 
    def general_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model    


class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"    


my_tesla=ElectricCar("Tesla","model s1","85KWh")

# print(isinstance(my_tesla,ElectricCar))
# print(isinstance(my_tesla,Car))

# print(my_tesla.brand)
# print(my_tesla.fuel_type())

# my_car=Car("Toyota","corolla")
my_car=Car("Tata","saffari")
# my_car.model="aura"
print(my_car.model)
# print(Car.total_car)
# print(my_car.fuel_type())

# print(my_car.general_description())
# print(Car.general_description())

# print(Car.total_car)

# print(my_car.brand)
# print(my_car.__brand)
# print(my_car.model)
# print(my_car.get_brand())
# print(my_car.full_name())
# my_new_car=Car("Tata","safari")
# print(my_new_car.model)


class Battery:
    def battery_info(self):
        return "This is battery Info"
    
class Engine:
    def engine_info(self):
        return "This is engine Info"


class Electric_car(Battery,Engine,Car):
    pass


my_new_tesla=Electric_car("Tesela","model SE")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())