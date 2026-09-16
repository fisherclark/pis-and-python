coins = [1, 5, 10, 25, 50, 100]

due = 50
coin = 0
while due > 0:
	print(f"Amount due: {due} cents")
	coin = int((input("Coin: ").strip().lower().strip(" cents")))
	if coin in coins:
		due -= coin
print(f"\nChange owed: {abs(due)} cents")
