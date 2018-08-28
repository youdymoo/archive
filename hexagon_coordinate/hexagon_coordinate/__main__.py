'''main python script of Hexagon Coordinate System.'''

import sys
import operator
import math

def isValid(hexagon):
    """returns if the given hexagon has a valid coordinate."""
    sum = 0
    for coord in hexagon:
        sum += coord
    if sum != 0: return False
    else: return True


def level(hexagon):
    """returns the level of the given hexagon."""    
    lev = 0
    for coord in hexagon:
        if abs(coord) > lev:
            lev = abs(coord)
    return lev


def quadrant(hexagon):
    """returns the quadrant of the given hexagon."""
    if isValid(hexagon) is False: return False

    if hexagon[0] == 0 and hexagon[1] == 0: return 'c'

    if hexagon[0] == 0: return 'x'
    elif hexagon[0] > 0:
        if hexagon[1] > 0: return 1
        elif hexagon[1] == 0: return 'y'
        else: 
            if hexagon[2] > 0: return 3
            elif hexagon[2] == 0: return 'z'
            else: return 2
    else:
        if hexagon[1] < 0: return 4
        elif hexagon[1] == 0: return 'y'
        else: 
            if hexagon[2] > 0: return 5
            elif hexagon[2] == 0: return 'z'
            else: return 6


def reduceAbs(value, i):
    """returns value with reduced absolute value."""
    if value > 0: value -= i
    elif value < 0: value += i
    return value


def delevel(hexagon, level):
    """returns neighbor hexagon(s) in the lower level of the given hexagon."""
    hex_list = []
    if level == 1:
        new_hex = []
        for coord in hexagon:
            new_hex.append(reduceAbs(coord, 1))
        hex_list = [tuple(new_hex)]
    elif level == 0:
        return [hexagon]
    else:
        indices = [0, 1, 2]
        for i in indices:
            if abs(hexagon[i]) == level: fix = i
        indices.pop(fix)
        for index in range(2):
            new_hex = {}
            new_hex[indices[index]] = reduceAbs(hexagon[indices[index]], 1)
            new_hex[fix] = reduceAbs(hexagon[fix], 1)
            new_hex[indices[(index + 1) % 2]] = hexagon[indices[(index + 1) % 2]]
            hex_list.append((new_hex[0], new_hex[1], new_hex[2]))
    return hex_list


def flow(hexagon):
    """returns hexagon(s) in the next flow direction of the given hexagon."""
    if isValid(hexagon) is False: return False

    quad = quadrant(hexagon)
    if quad in ['x', 'y', 'z']:
        return delevel(hexagon, 1)
    else:
        return delevel(hexagon, level(hexagon))


def test(hexagon1, hexagon2):
    """test in breadth first search."""
    if (isValid(hexagon1) or isValid(hexagon2)) is False: return False

    hex_list = [hexagon1]
    next_level = []
    dist = 0
    for tmp_hexagon in hex_list:
        next_level = flow(tmp_hexagon)
        hex_list.pop(0)
        dist += 1
        for next_level_hexagon in next_level:
            if next_level_hexagon == hexagon2:
                return dist
            hex_list.append(next_level_hexagon)
            print(hex_list)
    return dist


def translation(hexagon, center):
    """returns new coordinates of the given hexagon to the given new center."""
    return (hexagon[0] - center[0], hexagon[1] - center[1], hexagon[2] - center[2])


def distance(hexagon1, hexagon2):
    """returns relative distance between two given hexagons."""
    if (isValid(hexagon1) or isValid(hexagon2)) is False: return False
    return level(translation(hexagon1, hexagon2))


def angle(hexagon1, hexagon2):
    """returns angle between center and two given hexagons."""
    if (isValid(hexagon1) or isValid(hexagon2)) is False: return False

    dotproduct = sum((a * b) for a, b in zip(hexagon1, hexagon2))
    length1 = math.sqrt(sum((a * b) for a, b in zip(hexagon1, hexagon1)))
    length2 = math.sqrt(sum((a * b) for a, b in zip(hexagon2, hexagon2)))

    return math.acos(dotproduct / (length1 * length2))


def neighbor(hexagon):
    """returns neighbor hexagon(s) of the given hexagon."""
    if isValid(hexagon) is False: return False

    level_up = [(0, 1, -1), (1, 0 ,-1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0)]
    neighbors = []
    for up in level_up:
        neighbors.append(tuple(map(operator.add, hexagon, up)))
    return neighbors


def main():
    """API endpoints of Hexagon Coordinate System."""
    args = sys.argv[1:]
    test_tup = (1, -3, 2)
    test_tup_2 = (-3, 2, 1)

    if not args:
        print('usage: [-l(level)/-f(flow)/-t(translation)/-d(distance)/-n(neighbors)/-a(angle)]')
        sys.exit(1)
    elif args[0] == '-l':
        print(level(test_tup))
    elif args[0] == '-f':
        print(flow(test_tup))
    elif args[0] == '-t':
        print(translation(test_tup, test_tup_2))
    elif args[0] == '-d':
        print(distance(test_tup, test_tup_2))
    elif args[0] == '-n':
        print(neighbor(test_tup))
    elif args[0] == '-a':
        print(angle(test_tup, test_tup_2))

if __name__ == '__main__':
    main()
