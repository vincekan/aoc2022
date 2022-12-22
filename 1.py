"""
Part 1
Read through the file line by line.
If value exists, add to running sum.
If line is just a newline then append the running sum to a list of sums and reset the running sum.
List of sums corresponds to the total caloric load of each elf.
"""

sums = list()
runningSum = 0

with open("1input.txt", "r") as myfile:
    for line in myfile:
        if line == '\n':
            #skip
            sums.append(runningSum)
            runningSum = 0
        else:
            runningSum += int(line.strip())

answer1 = (max(sums))
print(answer1)

"""
Part 2
Use max() function to find top value, then remove it from the list.
Note that remove() only removes one item, even if there are duplicates. This is good.
Do this three times. Still O(n).
"""

answer2 = 0
cur_max = answer1

for _ in range(3):
    answer2 += cur_max
    sums.remove(cur_max)
    cur_max = max(sums)

print(answer2)