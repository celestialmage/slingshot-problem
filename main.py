def hittable_targets(room):
    # Your implementation here!
    auberon_coor = find_auberon(room)

    side_hits = check_hits(room[auberon_coor[0]], auberon_coor[1])

    target_column = [row[auberon_coor[1]] for row in room]

    verticle_hits = check_hits(target_column, auberon_coor[0])

    return side_hits + verticle_hits

def find_auberon(room):

    results = None

    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == 'A':
                results = (i, j)
                break

    return results

def check_hits(row, origin):
    
    hit_left = False
    left_index = origin

    while left_index >= 1 and hit_left is False:

        left_index -= 1

        if row[left_index] == 'T':
            hit_left = True
        elif row[left_index] == 'W':
            break

    row_length = len(row)
    hit_right = False
    right_index = origin

    while right_index <= row_length - 2 and hit_right is False:

        right_index += 1

        if row[right_index] == 'T':
            hit_right = True
        elif row[right_index] == 'W':
            break

    results = 0

    if hit_left:
        results += 1

    if hit_right:
        results += 1

    return results



room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]
assert hittable_targets(room1) == 2

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4

room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]
assert hittable_targets(room3) == 0

room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]
assert hittable_targets(room4) == 1

room5 = [
    ['A'],
]
assert hittable_targets(room5) == 0

print("All tests passed!")
print("If time remains, discuss time & space complexity")
