from Car import Car

car1 = Car("Red", "30", "100", "50")
car2 = Car("Yellow", "35", "105", "55")
print(f"The first car is {car1.colour}, it is travelling at {car1.currentSpeed},"
      f" it has a max speed of {car1.maxSpeed} and it has a fuel level of {car1.fuelLevel}")
print(f"The second car is {car2.colour}, it is travelling at {car2.currentSpeed},"
      f" it has a max speed of {car2.maxSpeed} and it has a fuel level of {car2.fuelLevel}")
car1.accelerate(110)
car2.brake(120)
car2.refuel(135)
print(f"The first car is {car1.colour}, it is travelling at {car1.currentSpeed},"
      f" it has a max speed of {car1.maxSpeed} and it has a fuel level of {car1.fuelLevel}")
print(f"The second car is {car2.colour}, it is travelling at {car2.currentSpeed},"
      f" it has a max speed of {car2.maxSpeed} and it has a fuel level of {car2.fuelLevel}")
