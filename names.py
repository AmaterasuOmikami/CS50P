name = input("Whats the name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()