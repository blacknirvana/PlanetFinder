import random
import time

#size
PlanetsizeMin = 6000
PlanetsizeMax = 7000
PlanetCounter = 0

#temperature
PlanetTempMin = 10
PlanetTempMax = 20

#earth
#size 6,371  km radius
#16c average

PlanetTimerStart = time.time()

while True:
    PlanetCounter += 1
    PlanetSizeValid = False
    PlanetTempValid = False

    PlanetSize = random.randrange(2440, 24622)
    if PlanetSize in range(PlanetsizeMin, PlanetsizeMax):
        PlanetSizeValid = True

     
    PlanetTemp = random.randrange(-233, 430)
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
print(f"Size: {PlanetSize} km radius")
print(f"Distance from its sun: xx t km")
print(f"CO2: xx%")
print(f"Temperature: {PlanetTemp}c")
print("-------------------------------")
print(PlanetTempValid)



