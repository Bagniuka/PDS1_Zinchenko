class Car:
    def __init__(self, brand, colour, engine_capacity):
        self.brand = brand
        self.colour = colour
        self.engine_capacity = engine_capacity

    def move_forward(self):
        print(f'Your {self.brand} is moving forward')
    def move_back(self):
        print(f'Your {self.brand} is moving back')

class ModifiedCar(Car):
    def turn_left(self):
        print(f'Your {self.brand} is turning left')
    def turn_right(self):
        print(f'Your {self.brand} is turning right')

ford_mustang = ModifiedCar('Ford', 'orange', 4951)
bmw_competition = Car('BMW', 'pink', 2993)



