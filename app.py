import random
import time

planets = [["AD33", random.randrange(1, 10), random.randrange(100000, 1000000000), random.randrange(1, 99), random.randrange(-1000, 1000)]]

print("-------------------------------")

for planet in planets:
    print(f"Name: {planet[0]}")
    print(f"Size: {planet[1]}")
    print(f"Distance from its sun: {planet[2]} t km")
    print(f"CO2: {planet[3]}%")
    print(f"Temperature: {planet[4]}c")
    print("-------------------------------")

sizeMin = 100
sizeMax = 1000
PlanetCounter = 0

PlanetTimerStart = time.time()

while True:
    PlanetSize = random.randrange(1, 50000)
    PlanetCounter += 1

    if sizeMin <= PlanetSize >= sizeMax:
        print(f" Planet #{PlanetCounter} out of range - {PlanetSize}")
    else:
        print(f"Planet #{PlanetCounter} is just right! - {PlanetSize}")
        break

PlanetTimerend = time.time()
PlanetTimer = PlanetTimerend - PlanetTimerStart

print(PlanetTimer)