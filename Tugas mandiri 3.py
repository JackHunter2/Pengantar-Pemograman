string = ""

bar = 5

while bar >= 1:
	kol = bar

	while kol > 0:
		string = string + str(kol) + " "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar - 1
	
print (string)
