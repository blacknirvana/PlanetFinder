import random

planets = [["AD33", random.randrange(1, 10), random.randrange(100000, 1000000000), random.randrange(1, 99), random.randrange(-1000, 1000)]]

print("-------------------------------")

for planet in planets:
    print(f"Name: {planet[0]}")
    print(f"Size: {planet[1]}")
    print(f"Distance from its sun: {planet[2]} t km")
    print(f"CO2: {planet[3]}%")
    print(f"Temperature: {planet[4]}c")
    print("-------------------------------")
