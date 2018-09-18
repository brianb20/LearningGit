print("Hello world!")
print("...")
print("Hello there!")
print("General Kenobi!")
i1 = input("Do you have the highground? (1 if yes 2 if no): ")
if int(i1) == 1:
	print("Automatic victory!")
if int(i1) == 2:
	i2 = input("Do you estimate your own power highly? (1 if yes 2 if no): ")
	if int(i2) == 1:
		print("You lost.")
	if int(i2) == 2:
		print("You survived, but did not win today.")
print("THE END")
