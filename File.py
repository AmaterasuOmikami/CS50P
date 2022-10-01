names = []

for _ in range(3):
    names.append(input("whats the name? "))

for name in sorted(names):
    print(f"hi, {name}")