import re
address = input("Address Line 1: ")
input("Address Line 2(apartment number, unit number): ")
city = input("City: ")
state = input("State: ")
zip = input("Zip Code: ")
states = ["al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
if re.fullmatch(r'\d+[a-zA-Z ]+', address) and re.fullmatch(r'[a-zA-Z\-]+', city) and state.strip().lower() in states and len(zip)==5:
	print("Valid Address!")
else:
	print("Invalid Address")
