"""
Part 1 & Part 2
Stream through the file and slices the input string into lengths of N.
Puts each slice into a set (eliminates duplicates).
Compares set size with N to find equality (meaning all unique chars in slice).

Probably not the most efficient but compact code.
N controlled by variable switch.
"""

# Stream through file
with open("6input.txt", "r") as myfile:
    line = next(myfile).strip("\n")  # takes line

# switch = 4   # for part 1
switch = 14  # for part 2

for i in range(len(line)):
    s = set(line[i:i + switch])
    if len(s) > switch - 1:
        print(i + switch)
        break
