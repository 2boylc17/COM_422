class CarPark:
    def __init__(self, capacity, bike_capacity):
        self.capacity = capacity
        self.registrations = []
        self.barrier = True
        self.bikeCapacity = bike_capacity

    def enter(self):
        print("What is the vehicle type? (1: Car  2: Motorbike  3:Emergency)")
        vehicle = int(input())
        if vehicle == 1:
            if len(self.registrations) < self.capacity:
                self.barrier = False
                print("What is the registration plate on the car?")
                reg = input()
                self.registrations.append(reg)
                print("Car has entered")
                self.barrier = True
            else:
                self.barrier = True
                print("No Entry. Car park is at capacity")
        if vehicle == 2:
            if len(self.registrations) < self.bikeCapacity:
                self.barrier = False
                print("What is the registration plate on the motorbike?")
                reg = input()
                self.registrations.append(reg)
                print("Motorbike has entered")
                self.barrier = True
            else:
                self.barrier = True
                print("No Entry. Car park is at capacity")
        if vehicle == 3:
            self.barrier = False
            reg = input()
            self.registrations.append(reg)
            self.barrier = True
        else:
            self.barrier = False
            print("This vehicle is not recognised by this Car Park")

    def leave(self):
        if len(self.registrations) <= 0:
            print("Error: No cars in car park")
        else:
            self.barrier = False
            print("What is the registration plate on the car?")
            reg = input()
            if reg in self.registrations:
                self.registrations.remove(reg)
                print("Car has left")
                self.barrier = True
            else:
                self.barrier = True
                print("This registration is not in the car park")
                self.leave()

    def view(self):
        print(f"The car park currently has {len(self.registrations)} occupants")


new = CarPark(15, 5)
