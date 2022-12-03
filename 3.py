'''
Part 1
Stream through the rucksack list and make a list of the duplicate item.
Then loop through the list and sum, using char numbering for priority.

Note: probably more efficient O(n) to stream through each char and append to dict,
and then find which dict k, v pair has v == 2.
This needs to be done per half of the bag, to discount duplicates in the same half bag.
'''

# finds duplicates from input of two lists by converting them to sets
def duplicate_finder(A, B):
    return set(A).intersection(set(B))

# finds priority of char input from a-z and A-Z
def priority_finder(c):
    if c.islower():
        return ord(c) - 96  # shifting ord to priority 1-26
    else:
        return ord(c) - 38  # shifting ord to priority 27-52

# Stream through and record rounds - O(n)
duplicates = []
with open("3input.txt", "r") as myfile:
    for line in myfile:
        mid = int(len(line.strip())/2)
        duplicates += duplicate_finder(line[:mid], line[mid:])

# Find total priority
total = 0
for c in duplicates:
    total += priority_finder(c)
print(total)



'''
Part 2
Utilising the functions above to make one further comparison. 
A bit messy due to returning a set and wanting to handle the calculation within the same loop,
necessitating conversion to string and stripping parentheses, etc.
More readable than a one-liner.
'''

# A different way to isolate all the elves into a list
elves = [line.strip('\n') for line in open("3input.txt")]

# Passing every group of 3 elves into the functions above
counter = 0
for i in range(0, len(elves), 3):
    val = duplicate_finder(duplicate_finder(elves[i], elves[i+1]), elves[i+2])
    counter += priority_finder(str(val).strip("{''}"))
print(counter)