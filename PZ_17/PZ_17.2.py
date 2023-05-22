# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


class Truck(Car):
    def __init__(self, brand, model, year, payload):
        super().__init__(brand, model, year)
        self.payload = payload

    def info(self):
        super().info()
        print(f"Грузоподъемность: {self.payload} тонн")


class PassengerCar(Car):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def info(self):
        super().info()
        print(f"Количество пассажиров: {self.passengers} человек")


truck1 = Truck("Volvo", "FH16", 2020, 20)
truck2 = Truck("MAN", "TGX", 2019, 18)

passenger_car1 = PassengerCar("Toyota", "Camry", 2015, 5)
passenger_car2 = PassengerCar("Audi", "A6", 2018, 4)

truck1.info()
truck2.info()

passenger_car1.info()
passenger_car2.info()