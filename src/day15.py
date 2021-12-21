from heapq import *

from day14 import calc_answer

class Node(object):
    def __init__(self, x: int, y: int, risk: int, max_x: int, max_y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.risk = risk
        self.expect = risk + (max_x - x + max_y - y - 2) #<< 2

    def __hash__(self) -> int:
        return self.x << 16 | self.y

    def __eq__(self, obj: object) -> bool:
        return obj.x == self.x and obj.y == self.y
    
    def __lt__(self, other: object) -> bool:
        return self.expect < other.expect

def node_risk(nodes: list[list[int]], x: int, y: int) -> int:
    max_x = len(nodes[0])
    max_y = len(nodes)
    x_1 = x % max_x
    y_1 = y % max_y
    d =  (x // max_x) + (y // max_y)
    r = (nodes[y_1][x_1] + d - 1) % 9 + 1
    return r

def path_risk(nums: list[list[int]], factor: int) -> int:
    max_x = len(nums[0]) * factor
    max_y = len(nums) * factor
    start = Node(0, 0, 0, max_x, max_y)
    end = Node(max_x-1, max_y-1, 0, max_x, max_y)
    nodes = [start]
    checked_nodes = set()
    while len(nodes) > 0:
        current = heappop(nodes)
        if current == end:
            break
        if current not in checked_nodes:
            if current.x < max_x - 1:
                x = current.x + 1
                y = current.y
                r = node_risk(nums, x, y)
                next = Node(x, y, current.risk + r, max_x, max_y)
                heappush(nodes, next)
            if current.y < max_y - 1:
                x = current.x
                y = current.y + 1
                r = node_risk(nums, x, y)
                next = Node(x, y, current.risk + r, max_x, max_y)
                heappush(nodes, next)
            if current.x > 0:
                x = current.x - 1
                y = current.y
                r = node_risk(nums, x, y)
                next = Node(x, y, current.risk + r, max_x, max_y)
                heappush(nodes, next)
            if current.y > 0:
                x = current.x
                y = current.y - 1
                r = node_risk(nums, x, y)
                next = Node(x, y, current.risk + r, max_x, max_y)
                heappush(nodes, next)
        checked_nodes.add(current)
    return current.risk

if __name__ == "__main__" :
    with open("input/day15.txt", "r") as f:
        lines = [l[0:-1] for l in f]
    nums = []
    for l in lines:
        nums.append([int(c) for c in l])
    
    # Part 1
    factor = 1
    print('Risk factor: ' + str(path_risk(nums, factor)))

    # Part 2
    factor = 5
    print('Risk factor: ' + str(path_risk(nums, factor)))
