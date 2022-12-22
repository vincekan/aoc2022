"""
Part 1
Stream through the file and take in the stacks as strings.
eg:
   X
A  Y
B  Z
becomes:
"AB"
"XYZ"

Then get to the actual 'moves' in the input and use regex to get the values.
After that, call function stack_mover to modify the strings in place.

Part 2
Copy the stacks and call a different function concurrently.
"""

import re


def stack_mover(qty, s1, s2):
    """
    Takes in a number of blocks to move from one stack to another.
    Uses string slicing and reversal to emulate moving block by block.

    :param qty: Integer number of blocks to move
    :param s1: String representing the stack to move from
    :param s2: String representing the stack to move to
    :return: The Strings after the operations
    """
    s2 += s1[-qty:][::-1]  # String reversal to emulate moving block by block
    s1 = s1[:-qty]
    return s1, s2


def stack_mover_mk2(qty, s1, s2):
    """
    Takes in a number of blocks to move from one stack to another.
    Uses string slicing and reversal to emulate moving in bulk.

    :param qty: Integer number of blocks to move
    :param s1: String representing the stack to move from
    :param s2: String representing the stack to move to
    :return: The Strings after the operations
    """
    s2 += s1[-qty:]  # Don't need this: [::-1]
    s1 = s1[:-qty]
    return s1, s2


# Stream through file
n = 8  # Hardcoded max height of stack at start - ugly but effective...
myString = ""
stack = []  # list of strings
with open("5input.txt", "r") as myfile:
    # Get the stacks
    lines = [next(myfile).strip("\n")[1::4] for x in range(n)]  # takes each line, removes \n, and takes every 4th char

    for i in range(len(lines[0])):
        for line in lines:
            myString += line[i]

    stacks = [myString[i:i + n] for i in range(0, len(myString), n)]
    stacks = [stack.strip()[::-1] for stack in stacks]
    stacks2 = stacks.copy()  # for Part 2

    # Skips next 2 lines of the file.
    next(myfile)
    next(myfile)

    # Takes each line uses regex to get the move of qty from s1 to s2
    # 'move qty from s1 to s2' becomes [qty, s1, s2]
    actions = [re.findall('[0-9]+', line.strip()) for line in myfile]

    # Call the functions with a[0] = qty, a[1] = s1, a[2] = s2
    for a in actions:
        stacks[int(a[1]) - 1], stacks[int(a[2]) - 1] = stack_mover(int(a[0]), stacks[int(a[1]) - 1],
                                                                   stacks[int(a[2]) - 1])
        stacks2[int(a[1]) - 1], stacks2[int(a[2]) - 1] = stack_mover_mk2(int(a[0]), stacks2[int(a[1]) - 1],
                                                                         stacks2[int(a[2]) - 1])

# Summing and displaying the final values
answer = answer2 = ''
for stack in stacks:
    answer += stack[-1]

for stack in stacks2:
    answer2 += stack[-1]

print(answer, answer2)
