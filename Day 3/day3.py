from statistics import mode

# PART 1 FUNCTIONS
def getGammaRate(inputList):
    values = [x for x in zip(*inputList)]
    gamma = [mode(x) for x in values]
    return gamma
            
def getEpsilonRate(gamma):
    for i in range(len(gamma)):
        epsilon = ["1" if i == "0" else "0" for i in gamma]
    return epsilon        

# PART 2 FUNCTIONS

#def mostCommon(inputList):
#    for i in range(len(inputList)):
#        inputList[i] = "".join([x for x in lines[i]])
#    
#def leastCommon():


def main():
    with open("day3.txt", "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    # SOLVING PART 1
    gammaRate = getGammaRate(lines)
    gammaRate = "".join(gammaRate)
    epsilonRate = getEpsilonRate(gammaRate)
    epsilonRate = int("".join(epsilonRate), 2)
    gammaRate = int(gammaRate, 2)
    
    powerConsumption = gammaRate * epsilonRate

    print(f"Gamma rate is: {gammaRate}\nEpsilon rate is: {epsilonRate}\nPower consumption is: {powerConsumption}")
    
    # SOLVING PART 2



if __name__ == "__main__":
    main()