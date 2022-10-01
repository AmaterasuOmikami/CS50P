name = input("Whats the name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
