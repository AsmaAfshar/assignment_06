#Create a class Engine and a class Car. Use composition by passing an Engine object to the 
# Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is starting..."

    def stop(self):
        return "Engine is stopping..."

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)

    def start(self):
        return f"{self.model} is starting. {self.engine.start()}"

    def stop(self):
        return f"{self.model} is stopping. {self.engine.stop()}"

# Example 
my_car = Car("Toyota Camry", 200)
print(my_car.start())
print(my_car.stop())
