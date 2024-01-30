class Car:
    def __init__(self, colour, current, maximum, fuel):
        self.colour = colour
        self.currentSpeed = int(current)
        self.maxSpeed = int(maximum)
        self.fuelLevel = int(fuel)

    def accelerate(self, value):
        new_speed = self.currentSpeed + value
        self.fuelLevel -= 1
        if self.fuelLevel < 0:
            print("Out of fuel")
        elif new_speed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed
            print("At maximum speed")
        elif value <= 0:
            print("Cannot accelerate by this value")
        else:
            self.currentSpeed = new_speed
            print(f"Speed increased by {value}")

    def brake(self, value):
        if self.currentSpeed - value <= 0:
            self.currentSpeed = 0
            print("Car is stationary")
        elif value <= 0:
            print("Cannot brake by this value")
        else:
            self.currentSpeed -= value
            print(f"Reduced speed by {value}")

    def refuel(self, value):
        if self.fuelLevel + value > 100:
            self.fuelLevel = 100
            print("At maximum fuel")
        elif value <= 0:
            print("Cannot refuel by this level")
        else:
            self.fuelLevel += value
            print(f"Refuelled by {value}")
