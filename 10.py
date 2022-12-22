"""
Part 1
Stream through the file and get moves.

Run through the list of commands:
1) Increment cycle count
2) Update the signal value V
3) Keep track of the previous value of V to simulate update at end of clock cycle

Use a list of threshold values to determine when to calculate the signal.
Add the signal to a rolling sum.

"""

# Stream through file
with open("10input.txt", "r") as myfile:
    # Get the stacks
    lines = [line.strip("\n").split() for line in myfile]

# Use this list as the stopping mechanism
target_vals = [x for x in range(20, 221, 40)]
curr_val = 1
result = cycle_count = 0

# Run through commands
for line in lines:
    # Exit condition: all the thresholds of interest are passed
    if len(target_vals) <= 0:
        break
    else:
        addval = 0
        if line[0] == 'noop':
            cycle_count += 1
        else:  # addx
            cycle_count += 2
            addval = int(line[1])

        last_val = curr_val
        curr_val += addval

        # Test for passing a threshold, if yes, sum
        if cycle_count >= min(target_vals):
            result += last_val * min(target_vals)
            target_vals.remove(min(target_vals))

print(result)

"""
Part 2

This time, use cycle count as the iterator, since we know the screen is 240 cycles long.
curr_val above is now the centroid of sprite location.
Update it only at the end of each addx command (2 cycles)

Append to a string to simulate the screen drawing.
Uses a helper function to determine what character to append at each cycle, 
based on the relative location of the cycle and the sprite.

"""


def which(string_length, sprite_position):
    """
    Takes in the string position and sprite position and checks if there is an overlap
    in order to determine what character to return for appending.

    :param string_length: int length of the string (aka, position being appended in the strong), 1-40
    :param sprite_position: int position of sprite
    :return: '#' if there is overlap, '.' otherwise
    """

    if string_length in range(sprite_position - 1, sprite_position + 2):
        return '#'
    else:
        return '.'


curr_val = 1  # centroid of sprite position
cycle_count = 0
result_str = ""

for line in lines:
    if cycle_count >= 240:
        break
    else:
        addval = 0
        if line[0] == 'noop':
            # Modulus required to simulate scanning through 6 rows of 40 chars wide in 240 char long str
            result_str += which(cycle_count % 40, curr_val)
            cycle_count += 1
        else:  # addx
            result_str += which(cycle_count % 40, curr_val)
            cycle_count += 1
            result_str += which(cycle_count % 40, curr_val)
            cycle_count += 1

            addval = int(line[1])

        curr_val += addval

for i in range(0, 241, 40):
    print(result_str[i:i + 40])
