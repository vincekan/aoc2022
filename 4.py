"""
Part 1
Stream through the list and send off each line to a comparator: isFullyContained.
Log results of comparator.

Part 2
Same as above but uses comparator: isNotOverlapping.
Idea is to identify the cases with no overlaps and then subtract from the total number of lines.

All above O(n).
"""


def isFullyContained(A, B):
    """
    Checks if A is a subset of B, if yes, returns True.
    There are two ways for this to occur:
    a0....b0........b1.a1
    b0..a0..a1.........b1

    :param A: A list of strings defining a range from A[0] to A[1]
    :param B: A list of strings defining a range from B[0] to B[1]
    :return: Boolean, True or False
    """
    return (a[0] <= b[0] and b[1] <= a[1]) or (a[0] >= b[0] and b[1] >= a[1])


def isNotOverlapping(A, B):
    """
    Checks if there is no overlap between A or B, if yes, returns True.
    There are two ways for this to occur:
    a0....a1........b0.b1
    b0..b1..a0.........a1

    :param A: A list of strings defining a range from A[0] to A[1]
    :param B: A list of strings defining a range from B[0] to B[1]
    :return: Boolean, True or False
    """
    return (a[1] < b[0]) or (b[1] < a[0])


# Stream through file and send off to comparators - O(n)
total_lines = fully_contained = not_overlapping = 0
with open("4input.txt", "r") as myfile:
    for line in myfile:
        # Do these cleaning operations once here, instead of twice in each of the comparators
        items = line.strip().split(",")
        a = list(map(int, items[0].split("-")))  # if this cast isn't performed then mistake due to str comparison!
        b = list(map(int, items[1].split("-")))

        # Send to comparators and log results
        if isFullyContained(a, b):
            fully_contained += 1
        if isNotOverlapping(a, b):
            not_overlapping += 1
        total_lines += 1

print(
    f'Of {total_lines} lines, {fully_contained} are fully contained and {total_lines - not_overlapping} are overlapping.')
