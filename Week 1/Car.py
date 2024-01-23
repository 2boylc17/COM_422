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
            self.currentSpeed = 0
            print("Out of fuel")
        elif self.currentSpeed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed
            print("At maximum speed")
        else:
            self.currentSpeed = new_speed
            print(f"Speed increased by {value}")

    def brake(self, value):
        self.currentSpeed -= value
        if self.currentSpeed < 0:
            self.currentSpeed = 0
            print("Car is stationary")
        else:
            print(f"Reduced speed by {value}")

    def refuel(self, value):
        self.fuelLevel += value
        if self.fuelLevel > 100:
            self.fuelLevel = 100
            print("At maximum fuel")
        else:
            print(f"Refuelled by {value}")
