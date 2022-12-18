'''
Part 1
Use regex to get the input.


'''

import re

def stack_mover(qty, s1, s2):
    s2 += s1[-qty:][::-1]
    s1 = s1[:-qty]
    return s1, s2

def stack_mover_mk2(qty, s1, s2):
    s2 += s1[-qty:]     # Don't need this: [::-1]
    s1 = s1[:-qty]
    return s1, s2


# Stream through file
n = 8   # Hardcoded max height of stack at start
myString = ""
stack = []  # list of strings
with open("5input.txt", "r") as myfile:
    lines = [next(myfile).strip("\n")[1::4] for x in range(n)]   # takes each line, removes \n, and takes every 4th char

    for i in range(len(lines[0])):
        for line in lines:
            myString += line[i]

    stacks = [myString[i:i+n] for i in range(0, len(myString), n)]
    stacks = [stack.strip()[::-1] for stack in stacks]
    stacks2 = stacks.copy()     #for Part 2

    # Skips next 2 lines of the file.
    next(myfile)
    next(myfile)

    # Takes each line uses regex to get the move of qty from s1 to s2
    actions = [re.findall('[0-9]+', line.strip()) for line in myfile]

    for a in actions:
        stacks[int(a[1])-1], stacks[int(a[2])-1] = stack_mover(int(a[0]), stacks[int(a[1])-1], stacks[int(a[2])-1])
        stacks2[int(a[1]) - 1], stacks2[int(a[2]) - 1] = stack_mover_mk2(int(a[0]), stacks2[int(a[1]) - 1],
                                                                   stacks2[int(a[2]) - 1])

answer = answer2 = ''
for stack in stacks:
    answer += stack[-1]

for stack in stacks2:
    answer2 += stack[-1]

print(answer, answer2)

