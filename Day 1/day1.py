"""
As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen,
the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried 
into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)

"""
#PART 1
sumPartOne = 0

with open("day1.txt", "r") as f:
    lines =  [int(x) for x in f.readlines()]
 
for i in range(len(lines)):
    if lines[i] > lines[i-1]:
        sumPartOne += 1

print(f"Part 1 solution is: {sumPartOne}")


"""
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window.
"""

#PART 2

sumPartTwo = 0

"""
OLD WAY 

for i in range(3, len(lines)):
    
    if lines[i] > lines[i-3]:
        sumPartTwo += 1
"""
#using zip()
sumPartTwo=sum(first<second for first,second in zip(lines, lines[3:]))

print(f"Part 2 solution is: {sumPartTwo}")