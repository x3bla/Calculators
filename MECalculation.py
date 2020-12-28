# Made by x3bla
# FTB Revelation 3.4.0
# Minecraft ver 1.12.2


# declaring materials
skyStone = 0
glowDust = 0
fluixCrystalDust = 0
iron = 0
quartzGlass = 0
pureFluixCrystal = 0
redstone = 0
certQuartz = 0
meOne = 0
meFour = 0
meOneSix = 0
meSixFour = 0
calPro = 0
engPro = 0
logPro = 0
meCable = 0
storageHousing = 0
netherQuartz = 0
craftingTable = 0
fluixCrystal = 0


# Main block of the ME System
# Energy accepter
mainBlock = int(input("Input 1 for Energy Accepter, input 2 for ME Controller, input 3 to skip\n"))
if mainBlock == 1:
    iron += 4
    quartzGlass += 4
    fluixCrystal += 1

# ME Controller
if mainBlock == 2:
    skyStone += 4
    pureFluixCrystal += 4
    engPro += 1



# ME Drive
for x in range(int(input("How much ME Drive do you require? (Recommended for beginners: 1)\n"))):
    engPro += 2
    meCable += 2
    iron += 4

# amount of materials needed for the housing

for x in range(int(input("How many cells are you going to make now?\n"))):
    redstone += 3
    quartzGlass += 2
    iron += 3

# amount of 64k to make
if input("Will you be making 64k cells? (y/n)\n").lower() == 'y':
    meSixFour += int(input("How much 64k cells are you making?\n"))
    
# amount of 16k to make
if input("Will you be making 16k cells? (y/n)\n").lower() == 'y':
    meOneSix += int(input("How much 16k cells are you making?\n"))

# amount of 4k to make
if input("Will you be making 4k cells? (y/n)\n").lower() == 'y':
    meFour += int(input("How much 4k cells are you making?\n"))

# amount of 1k to make
if input("Will you be making 1k cells? (y/n)\n").lower() == 'y':
    meOne += int(input("How much 1k cells are you making?\n"))

# Terminal or crafting terminal
terminalCheck = int(input("Input 1 for ME Terminal, input 2 for ME Crafting Terminal, input 3 to skip\n"))
if terminalCheck == 1:
    fluixCrystalDust += 2
    certQuartz +=1
    netherQuartz += 1
    logPro += 3
    redstone += 1
    quartzGlass += 3
    glowDust += 2
    iron += 1

if terminalCheck == 2:
    craftingTable += 1
    calPro += 1
    fluixCrystalDust += 2
    certQuartz +=1
    netherQuartz += 1
    logPro += 3
    redstone += 1
    quartzGlass += 3
    glowDust += 2
    iron += 1

# 64k storage component
for x in range(meSixFour):
    meOneSix += 3
    glowDust += 4
    quartzGlass += 1
    calPro += 1
    
# 16k storage component
for x in range(meOneSix):
    glowDust += 4
    meFour += 3
    quartzGlass += 1
    calPro += 1

# 4k storage component
for x in range(meFour):
    redstone += 4
    calPro += 1
    meOne += 3
    quartzGlass += 1

# 1k storage component
for x in range(meOne):
    redstone += 4
    certQuartz += 4
    logPro += 1



# printing the results
# making a lot of print lines because I don't like seeing one very long line
print("\n\nThe total material that you need")
print("Sky Stone:", skyStone)
print("Glowstone Dust:", glowDust)
print("Fluix Crystal Dusts:", fluixCrystalDust)
print("Iron:", iron)
print("Quartz Glass:", quartzGlass)
print("Pure Fluix Crystal", pureFluixCrystal)
print("Redstone:", redstone)
print("Certus Quartz:", certQuartz)
print("ME Cable:", meCable)
print("Nether Quartz:", netherQuartz)
print("Crafting Table:", craftingTable)
print("Fluix Crystal:", fluixCrystal)
print("\nFor reference, you will need(calculations below)")
print("Calculation Processor:", calPro)
print("Engineering Processor:", engPro)
print("Logical Processor:", logPro)
print("\n")
print("1K ME component:", meOne)
print("4K ME component:", meFour)
print("16K ME component:", meOneSix)
print("64K ME component:", meSixFour)


# materials for processors
# declaring materials
proPureCert = 0
proRedstone = 0
proSilicon = 0
proGold = 0
proDiamond = 0

# calculating materials needed
for x in range(logPro):
    proSilicon += 1
    proGold += 1
    proRedstone += 1

for x in range(engPro):
    proRedstone += 1
    proDiamond += 1
    proSilicon += 1

for x in range(calPro):
    proRedstone += 1
    proPureCert += 1
    proSilicon += 1

print("\n\nFor the processors, you require")
print("Pure Certus Quartz:", proPureCert)
print("Redstone:", proRedstone)
print("Silicon:", proSilicon)
print("Gold:", proGold)
print("Diamond:", proDiamond)
print("\nCalculation Processor:", calPro, "\nEngineering Processor:", engPro, "\nLogic Processor:", logPro)
