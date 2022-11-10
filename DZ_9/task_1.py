class Car:
    def __init__(self, brand, colour, engine_capacity):
        self.brand = brand
        self.colour = colour
        self.engine_capacity = engine_capacity

    def move_forward(self):
        print('Your car is moving forward')
    def move_back(self):
        print('Your car is moving back')

class ModifiedCar(Car):
    def turn_left(self):
        print('Your car is turning left')
    def turn_right(self):
        print('Your car is turning right')

ford_mustang = ModifiedCar('Ford', 'orange', 4951)
bmw_competition = Car('BMW', 'pink', 2993)



