"""
DAY 2

"""

#PART 1

with open("day2.txt", "r") as file:
    lines = file.readlines()

newList = []
forwardPosition = 0
depthPosition = 0

for i in range(len(lines)):

    newList.append(lines[i].split())
    newList[i][1] = int(newList[i][1])

    if newList[i][0] == "forward":
        forwardPosition = forwardPosition + newList[i][1]

    else:
        if newList[i][0] == "down":
            depthPosition = depthPosition + newList[i][1]
        if newList[i][0] == "up":
            depthPosition = depthPosition - newList[i][1]

resultPartOne  = forwardPosition * depthPosition

print(f"Forward: {forwardPosition} -- Depth: {depthPosition} -- Product: {resultPartOne}")

#PART 2

forwardPositionPartTwo = 0
depthPositionPartTwo = 0

aim = 0

for i in range(len(newList)):

    if newList[i][0] == "down":
        aim = aim + newList[i][1]
        

    elif newList[i][0] == "up":
        aim = aim - newList[i][1]

    elif newList[i][0] == "forward":
        forwardPositionPartTwo += newList[i][1]
        depthPositionPartTwo += aim * newList[i][1]

    print(f"AIM: {aim}")
    print(f"FORWARD: {forwardPositionPartTwo}")
    print(f"DEPTH: {depthPositionPartTwo}")
    print("~ ~ # # # ~ ~")

resultPartTwo = forwardPositionPartTwo * depthPositionPartTwo

print(f"Forward: {forwardPositionPartTwo} -- Depth: {depthPositionPartTwo} -- Product: {resultPartTwo}")

