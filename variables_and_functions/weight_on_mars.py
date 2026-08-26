def calculate_mercury_weight(weight):
	weight = 0.377*weight
	return weight
def calculate_venus_weight(weight):
	weight = 0.907*weight
	return weight
def calculate_mars_weight(weight):
	weight = 0.378*weight
	return weight
def calculate_jupiter_weight(weight):
	weight = 2.528*weight
	return weight
def calculate_saturn_weight(weight):
	weight = 1.064*weight
	return weight
def calculate_uranus_weight(weight):
	weight = 0.889*weight
	return weight
def calculate_neptune_weight(weight):
	weight = 1.125*weight
	return weight

e_weight = int(input("Earth Weight: "))
planet = input("New planet: ")
if planet.strip().lower() == "mercury":
	weight = calculate_mercury_weight(e_weight)
elif planet.strip().lower() == "venus":
	weight = calculate_venus_weight(e_weight)
elif planet.strip().lower() == "mars":
	weight = calculate_mars_weight(e_weight)
elif planet.strip().lower() == "jupiter":
	weight = calculate_jupiter_weight(e_weight)
elif planet.strip().lower() == "saturn":
	weight = calculate_saturn_weight(e_weight)
elif planet.strip().lower() == "uranus":
	weight = calculate_mars_weight(e_weight)
elif planet.strip().lower() == "neptune":
	weight = calculate_mars_weight(e_weight)
else:
	print("Not a planet.")
print(f"{planet.strip().title()} Weight: {weight}")
