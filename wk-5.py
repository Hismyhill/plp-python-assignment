# Solution 1

class Smartphone:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def click(self):
        print("Smile to the camera!")

class Sony(Smartphone):
    def __init__(self, color, model):
        super().__init__(color, model)

    def click(self):
        print("Sony click sound 📸")

class Samsung:
      def snap(self):
       return "Samsung click sound 📸"

class Iphone:
      def snap(self):
       return "iPhone click sound 📸"


xperia = Sony("white", "Xperia") 
samsung = Smartphone("black", "Samsung")
iphone = Smartphone("gold", "iPhone")

xperia.click()
print(f"This is a {xperia.color} Sony {xperia.model}")

for phone in [Samsung(), Iphone()]:
    print(phone.snap())

# Solution 2
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

for vehicle in [Car(), Plane()]:
    print(vehicle.move())