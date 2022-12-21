'''
Part 1
Stream through the file and get moves.

Use a list of x, y coordinates to record the location of H and T.

At each command (line):
At each move (1 unit in magnitude change):
Save the last position of H and move it.
Check distance from T to see if a move is required.
If yes, move T to the last position of H.

At end of each move, record where the tail is in a dict for uniqueness.

'''

def nearby(h, t):
    '''
    Function takes in the head and tail lists and checks if they are within 1 cell distance.
    Uses a one liner to determine if the x, y coordinates are within +/- 1 grid

    :param h: List of x, y coordinate of Head
    :param t: List of x, y coordinate of Tail
    :return: Boolean, True or False
    '''
    return h[0] in range(t[0]-1, t[0]+2) and h[1] in range(t[1]-1, t[1]+2)

# Stream through file
with open("9input.txt", "r") as myfile:
    # Get the stacks
    lines = [line.strip("\n").split() for line in myfile]

# Model the location of the head and tail in x, y coordinates
head = [0, 0]
tail = [0, 0]
tail_locs = dict()

for line in lines:
    direction, magnitude = line[0], int(line[1])

    for move in range(magnitude):
        last = head.copy()  # Save the last known head location, this is where T will follow

        # Determine the move to make
        if direction == 'D':
            head[1] -= 1
        elif direction == 'U':
            head[1] += 1
        elif direction == 'L':
            head[0] -= 1
        else:
            head[0] += 1

        # After the move, check if T needs to catch up
        if not nearby(head, tail):
            tail = last.copy()
            tail_locs.update({str(tail): 1})

# Keys are unique. Add 1 for [0, 0].
print(len(tail_locs.keys()) + 1)

'''
Part 2
Can't use the same 'last position' trick now that we have a big chain.

At each command (line):
At each move (1 unit in magnitude change):
At each knot (10 now!), check:
- touching, if yes, do nothing and skip to next move, otherwise,
- check diagonal or not, if diagonal, move diagonal

At end of each move, record where the tail is in a dict for uniqueness.

'''

def getMove(h, t):
    '''
    Function takes in the head and tail lists and uses the delta in x, y coordinates
    to return a suitable move for the tail to catch up.
    As all moves are single steps, uses delta/abs(delta) to determine the correct vector in each axis.

    :param h: List of x, y coordinate of Head
    :param t: List of x, y coordinate of Tail
    :return: List of x, y coordinate of movement vector
    '''
    dx = h[0] - t[0]
    dy = h[1] - t[1]

    if dx == 0:
        return [0, int(dy/abs(dy))]
    elif dy == 0:
        return [int(dx/abs(dx)), 0]
    else:
        return [int(dx/abs(dx)), int(dy/abs(dy))]

# Model the location of the 10 knots in x and y coordinates
snake = [[0, 0] for _ in range(10)]
tail_locs2 = dict()

# Iterate through commands
for line in lines:
    direction, magnitude = line[0], int(line[1])

    # Iterate through moves
    for move in range(magnitude):

        # Determine the move to make for the head knot
        if direction == 'D':
            snake[0][1] -= 1
        elif direction == 'U':
            snake[0][1] += 1
        elif direction == 'L':
            snake[0][0] -= 1
        else:
            snake[0][0] += 1

        # Iterate through remaining knots in snake, indices 1 to 9
        for knot in range(1, 10):
            # Check if next knot needs to catch up
            if nearby(snake[knot-1], snake[knot]):
                # Do nothing, no need to update any further
                break
            else:
                # Get the move for the know to catch up and apply it
                move = getMove(snake[knot-1], snake[knot])
                snake[knot][0] += move[0]
                snake[knot][1] += move[1]

        tail_locs2.update({str(snake[-1]): 1})

# Keys are unique. No need to add 1 for [0, 0], as it is picked up on first loop.
print(len(tail_locs2.keys()))