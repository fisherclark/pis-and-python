class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
	def __init__(self, receipt):
		self.receipt = receipt
	def add_item(self, item):
		self.receipt.append(item)
	def calculate_taxes(self):
		sum = 0
		for i in self.receipt:
			sum += i.price
		sum *= 0.07
		sum = round(sum, 2)
		return(sum)
	def calculate_total(self):
		sum = 0
		for i in self.receipt:
			sum += i.price
		sum *= 1.07
		sum = round(sum, 2)
		return(sum)
	def print_receipt(self):
		print("CROSSROAD'S CAFE\n----------------")
		for i in self.receipt:
			print(f"{i.name}: {i.price:0.2f}")
		print(f"----------------\ntaxes: {self.calculate_taxes()}\n----------------\ntotal: {self.calculate_total()}")
def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total()
   print("The total due is " + str(total))

   order1.print_receipt()
   

if __name__ == '__main__':
	main()
