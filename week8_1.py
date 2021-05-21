# MIS 132 - May 21
# Vehicle, Car Classes

class Vehicle:
    """
    It's a simple vehicle class with speedup and slowdown methods.
    """
    def __init__(self, max_passengers, wheels=4, current_speed=100):
        self.max_passengers = max_passengers
        self.wheels = wheels
        self.current_speed = current_speed

    def speedup(self):
        if self.current_speed >= 180:
            print("You cannot exceed the speed limit.")
        else:
            self.current_speed += 10
            print(f"Now you are at {self.current_speed} km/h.")

    def slowdown(self):
        if self.current_speed <= 0:
            print("The vehicle is already stopped.")
        else:
            self.current_speed -= 10
            print(f"Now you are at {self.current_speed} km/h.")
            if self.current_speed == 0:
                print("The vehicle is stopped!")

    def __str__(self):
        return f"The vehicle is at {self.current_speed} km/h. The max passenger is {self.max_passengers}."

my_vehicle = Vehicle(4,4)
#print(my_vehicle)
#for i in range(0,13):
#    my_vehicle.slowdown()


class Motorcycle(Vehicle):

    def __init__(self, max_passengers, wheels, current_speed, manufacturer, top_speed):
        Vehicle.__init__(self, max_passengers, wheels, current_speed)
        self.manufacturer = manufacturer
        self.top_speed = top_speed

new_motor = Motorcycle(2,2,100,"Honda", 200)

class Car(Vehicle):

    def __init__(self, max_passengers, wheels, current_speed, manufacturer, top_speed, num_doors, modelyear, color, style):
        Vehicle.__init__(self, max_passengers, wheels, current_speed)
        self.manufacturer = manufacturer
        self.top_speed = top_speed
        self.num_doors = num_doors
        self.modelyear = modelyear
        self.color = color
        self.style = style
        self.engine_status = True

    def change_color(self, color):
        self.color = color
        print(f"Your car's new color is {self.color}.")

    def stop_engine(self):
        self.engine_status = False
        print("The engine has stopped.")

    def start_engine(self):
        self.engine_status = True
        print("The engine has started.")

    def speedup(self):
        if self.engine_status:
            if self.current_speed >= 180:
                print("You cannot exceed the speed limit.")
            else:
                self.current_speed += 10
                print(f"Now you are at {self.current_speed} km/h.")
        else:
            print("You didn't start your car. :( ")

    def slowdown(self):
        if self.engine_status:
            if self.current_speed <= 0:
                print("The vehicle is already stopped.")
            else:
                self.current_speed -= 10
                print(f"Now you are at {self.current_speed} km/h.")
                if self.current_speed == 0:
                    print("The vehicle is stopped!")
        else:
            print("You didn't start your car. :( ")



#new_car = Car(4,4,100,"Honda", 240, 5, 2010, "red", "sedan")
#new_car.change_color("black")

#new_car.slowdown()
#new_car.stop_engine()

#new_car.speedup()
#new_car.start_engine()
#new_car.speedup()
#new_car.speedup()
