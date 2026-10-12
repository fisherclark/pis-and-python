class Car:
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg

def main():
	car1 = Car("Toyota", "Prius", 35)
	car2 = Car("Subaru","Outback", 32)
	car3 = Car("Ford", "F150", 25)
	
	parking_lot = [car1, car2, car3]
	
	sum = 0
	for i in parking_lot:
		sum += i.mpg
	print(f"Total: {sum} mpg")

if __name__ == '__main__':
	main()
