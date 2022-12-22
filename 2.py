"""
Part 1
Stream through the strategy guide and increment two counters:
    1. Counter for what you played (X, Y, Z)
    2. Counter for if you won or lost
Use dictionary to keep tally and multiply through at the end.
(instead of incrementing score - cleaner code).
"""

# Stream through and record rounds - O(n)
round = {}
with open("2input.txt", "r") as myfile:
    for line in myfile:
        if line[:-1] in round: #low cost strip of newline
            round[line[:-1]] += 1
        else:
            round[line[:-1]] = 1

# Build score key
key = {}
for k, v in round.items():
    if k[-1] == "X":
        key[k] = 1 # you used rock
        if k[0] == "A":
            key[k] += 3 #tie
        elif k[0] == "B":
            key[k] += 0 #loss
        else:
            key[k] += 6 #win
    elif k[-1] == "Y":
        key[k] = 2 # you used paper
        if k[0] == "A":
            key[k] += 6 #win
        elif k[0] == "B":
            key[k] += 3 #tie
        else:
            key[k] += 0 #loss
    else:
        key[k] = 3 # you used scissors
        if k[0] == "A":
            key[k] += 0 #loss
        elif k[0] == "B":
            key[k] += 6 #win
        else:
            key[k] += 3 #tie

# Calculate final score
score = 0
for k, v in round.items():
    score += v * key[k]

print(f'Part 1: {score}')


"""
Part 2
Basically just a new scoring system.
X, Y, Z already tells you the outcome.
A, B, C evaluated to tell yu what you played to achieve the outcome.
Build a new key dict.
"""

# Build score key
key2 = {}
for k, v in round.items():
    if k[-1] == "X":
        key[k] = 0 # you lost
        if k[0] == "A":
            key[k] += 3 #Z
        elif k[0] == "B":
            key[k] += 1 #X
        else:
            key[k] += 2 #Y
    elif k[-1] == "Y":
        key[k] = 3 # you drew
        if k[0] == "A":
            key[k] += 1 #X
        elif k[0] == "B":
            key[k] += 2 #Y
        else:
            key[k] += 3 #Z
    else:
        key[k] = 6 # you won
        if k[0] == "A":
            key[k] += 2 #Y
        elif k[0] == "B":
            key[k] += 3 #Z
        else:
            key[k] += 1 #X

# Calculate final score
score = 0
for k, v in round.items():
    score += v * key[k]

print(f'Part 2: {score}')