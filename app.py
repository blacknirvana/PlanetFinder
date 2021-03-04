import random
import time

#size
PlanetsizeMin = 100
PlanetsizeMax = 500
PlanetCounter = 0

#temperature
PlanetTempMin = 15
PlanetTempMax = 100

PlanetTimerStart = time.time()

while True:
    PlanetCounter += 1
    PlanetSizeValid = False
    PlanetTempValid = False

    PlanetSize = random.randrange(1, 50000)
    if PlanetSize in range(PlanetsizeMin, PlanetsizeMax):
        PlanetSizeValid = True

     
    PlanetTemp = random.randrange(-5000, 5000)
    if PlanetTemp in range(PlanetTempMin, PlanetTempMax):
        PlanetTempValid = True


    if PlanetSizeValid and PlanetTempValid:
        print(f"Planet #{PlanetCounter} is good!")
        break



PlanetTimerend = time.time()
PlanetTimer = PlanetTimerend - PlanetTimerStart

print(PlanetTimer)

print("-------------------------------")

print(f"Name: XXXX")
print(f"Size: {PlanetSize}")
print(f"Distance from its sun: xx t km")
print(f"CO2: xx%")
print(f"Temperature: {PlanetTemp}c")
print("-------------------------------")
print(PlanetTempValid)



