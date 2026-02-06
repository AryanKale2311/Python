class vehicle:
    def move(self):
        print("This vehicle is moving")

class Car(vehicle):
    def move(self):
        print ("Driving on the road")

class Bicycle(vehicle):
    def move(self):
        print ("Pedaling on the road ")

vehicles =  [vehicle(),Car(),Bicycle()]
for vehicle in vehicles:
    print(vehicle.move())