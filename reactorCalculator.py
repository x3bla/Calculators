# by x3bla
# FTB Rev 2.4.0


import math


def ControlRods(x):
    n = x
    ans = 2.5 - (2 *x) + (0.5 * math.pow(x, 2))
    return int(ans)

def Casing(x):
    X = x*x*x
    Y = (x-2)*(x-2)*(x-2)
    return X-Y

def ConvertToStack(x):
    stack = x // 64
    remainder = x % 64
    return stack, remainder

def ConvertToStack(x):
    stack = x // 64
    remainder = x % 64
    return stack, remainder



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

# declaring upgrade materials
newReactorCasing = 0
newGraphite = 0
newUranium = 0
newRedstone = 0
newPiston = 0
newChest = 0
newHopper = 0
newDiamond = 0
newComparator = 0
newGlass = 0
newIron = 0
newGold = 0
newReactorCasingCore = 0

# note
print("Note that i'm using a checkered pattern for the rods so the reactor size only works with odd numbers\n\n")

# upgrading current or making new reactor
upgradeCheck = False
if input("input 1 if you're making a new reactor, input 2 if you are upgrading your reactor to a larger size\n") == '1':
    upgradeCheck = False
else:
    upgradeCheck = True

# size of the reactor
if upgradeCheck == True:
    size = int(input("How big is your current reactor size? (input '5' for 5x5x5, etc)\n"))
else:
    size = int(input("How big do you want the reactor to be? (input '5' for 5x5x5, etc, select an odd number)\n"))

# need main blocks or no
if upgradeCheck == False:
    mainBlockCheck = input("Do you already have the essential components? Y/N (Controller, power tap, 2 access port)\n")
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
for x in range(ControlRods(size)):
    reactorCasing += 4
    piston += 1
    redstone += 1
    uranium += 1
    graphite += 1

# because 4 blocks are taken by the main blocks
reactorCasing -= 4

# casings needed and materials
totalCasing = Casing(size) + reactorCasing
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
fuelRod = ControlRods(size)*(size-2)
for x in range(fuelRod):
    iron += 4
    graphite += 2
    glass += 2
    uranium += 1

## Reactor upgrade calculation (basically a copy paste, how do i make this more efficient)

# new size of the reactor
if upgradeCheck == True:
    newSize = int(input("How big do you want the new reactor to be? (input '5' for 5x5x5, etc. select an odd number)\n"))

    # control rods and materials needed for upgrade
    for x in range(ControlRods(newSize)):
        newReactorCasing += 4
        newPiston += 1
        newRedstone += 1
        newUranium += 1
        newGraphite += 1

    # because 4 blocks are taken by the main blocks
    newReactorCasing -= 4

    # casings needed and materials
    newTotalCasing = Casing(newSize) + newReactorCasing
    for x in range(newTotalCasing):
        newReactorCasingCore += 1
        newIron += 4
        newGraphite += 4

    newCasingCheck = newTotalCasing%4
    if newCasingCheck != 0:
        newCasingCore = newTotalCasing + 1
    else:
        newCasingCore = newTotalCasing

    for count in range(newCasingCore):
        newGold += 2
        newIron += 4
        newGraphite += 2
        newRedstone += 1

    # fuel rods needed and materials
    newFuelRod = ControlRods(newSize)*(newSize-2)
    for x in range(newFuelRod):
        newIron += 4
        newGraphite += 2
        newGlass += 2
        newUranium += 1

# for the upgrade
if upgradeCheck == True:
    graphite = newGraphite - graphite
    uranium = newUranium - uranium
    redstone = newRedstone - redstone
    piston = newPiston - piston
    glass = newGlass - glass
    iron = newIron- iron
    gold = newGold - gold
    reactorCasingCore = newReactorCasingCore - reactorCasingCore
    totalCasing = newTotalCasing - totalCasing

# displaying the info

print("\nGraphite:", graphite, ConvertToStack(graphite))
print("Uranium:", uranium, ConvertToStack(uranium))
print("Redstone:", redstone, ConvertToStack(redstone))
print("Piston:", piston, ConvertToStack(piston))
print("Chest:", chest)
print("Hopper:", hopper)
print("Diamond:", diamond)
print("Comparator:", comparator)
print("Glass:", glass, ConvertToStack(glass))
print("Iron:", iron, ConvertToStack(iron))
print("Gold:", gold, ConvertToStack(gold))
print("\nTotal Reactor Casing Core for reference:", reactorCasingCore, ConvertToStack(reactorCasingCore))
print("Total Reactor Casing for reference:", totalCasing, ConvertToStack(totalCasing))
