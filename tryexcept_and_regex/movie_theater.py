movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Lord Of The Rings", "12 Angry Men", "Schindler's List", "Pulp Fiction"]
tickets = {
	"Adult": 15,
	"Teen": 12,
	"Child": 5,
}
movie = ""
price = 0
while not movie.title() in movies:
	movie = input("Movie: ")
	if not movie.title() in movies:
		print("Invalid movie")
print("---")
try:
	while True:
		ticket = input("Ticket type: ")
		if ticket.title() in tickets:
			price += tickets[ticket.title()]
		else:
			print("Invalid ticket type")
except EOFError:
	print("\n---")
print(f"You are seeing {movie.upper()} and your total is ${str(price)+'.00'}.")
