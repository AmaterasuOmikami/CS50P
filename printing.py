# just a test program
name = input("What's your name? ")
name = name.strip().title()
first, last = name.split(" ")

print(f"Hello, {first}, thats cool")

age = input("How old are you? ")
age = age.strip()

print("Wow, " + age + "?!" + " You're old", end="")
print(" \"HAHAHA\"")
