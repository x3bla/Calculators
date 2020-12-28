# by x3bla

def controlRods(x):
    n = x-4
    ans = n * n + (n + 1) * (n + 1)
    return ans

def casing(x):
    X = x*x*x
    Y = (x-2)*(x-2)*(x-2)
    return X-Y

# declaring materials
reactorCasing = 0
graphite = 0
uranium = 0
redstone = 0
piston = 0
chest = 0
hopper = 0
diamond = 0
comparator = 0
glass = 0
iron = 0
gold = 0
reactorCasingCore = 0

# declaring other variables


# size of the reactor
size = int(input("How big do you want the reactor to be? (input '5' for 5x5x5, etc)\n"))

# need main blocks or no
mainBlockCheck = input("Do you already have the essential components? Y/N (Controller, power tap, etc)\n")
if mainBlockCheck.lower() == 'n':
    # controller block
    uranium += 2
    diamond += 1
    comparator += 1
    redstone += 1
    reactorCasing += 4

    # power tap
    redstone += 13
    reactorCasing += 4

    # access port x2
    reactorCasing += 8
    chest += 2
    iron += 4
    hopper += 2
    piston += 2

# control rods needed and materials
for x in range(controlRods(size)):
    reactorCasing += 4
    piston += 1
    redstone += 1
    uranium += 1
    graphite += 1

# because 4 blocks are taken by the main blocks
reactorCasing -= 4

# casings needed and materials
totalCasing = casing(size) + reactorCasing
for x in range(totalCasing):
    reactorCasingCore += 1
    iron += 4
    graphite += 4

casingCheck = totalCasing%4
if casingCheck != 0:
    casingCore = totalCasing + 1
else:
    casingCore = totalCasing

for count in range(casingCore):
    gold += 2
    iron += 4
    graphite += 2
    redstone += 1

# fuel rods needed and materials
fuelRod = controlRods(size)*(size-2)
for x in range(fuelRod):
    iron += 4
    graphite += 2
    glass += 2
    uranium += 1

# displaying the info

print("\nGraphite:", graphite)
print("Uranium:", uranium)
print("Redstone:", redstone)
print("Piston:", piston)
print("Chest:", chest)
print("Hopper:", hopper)
print("Diamond:", diamond)
print("Comparator:", comparator)
print("Glass:", glass)
print("Iron:", iron)
print("Gold:", gold)
print("\nTotal Reactor Casing Core for reference:", reactorCasingCore)
print("Total Reactor Casing for reference:", totalCasing) 











