class Point(object):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return self.x << 16 | self.y

    def __eq__(self, obj: object) -> bool:
        return obj.x == self.x and obj.y == self.y

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Line(object):
    def __init__(self, p1: Point, p2: Point) -> None:
        super().__init__()
        if (p1.x < p2.x) or (p1.x == p2.x and p1.y < p2.y):
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

    def isHorizontal(self):
        return self.p1.y == self.p2.y

    def isVertical(self):
        return self.p1.x == self.p2.x
    
    def getPoints(self) -> list[Point]:
        result = []
        if self.isHorizontal():
            for i in range(self.p1.x, self.p2.x + 1):
                result.append(Point(i, self.p1.y))
        elif self.isVertical():
            for i in range(self.p1.y, self.p2.y + 1):
                result.append(Point(self.p1.x, i))
        else:
            if self.p1.y < self.p2.y:
                inc = 1
            else:
                inc = -1
            y = self.p1.y
            for i in range(self.p1.x, self.p2.x + 1):
                result.append(Point(i, y))
                y += inc
        return result

def parse_lines(data: list[str]) -> list[Line]:
    result = []
    for row in data:
        s1, s2 = row.split(" -> ")
        x1, y1 = s1.split(",")
        p1 = Point(int(x1), int(y1))
        x2, y2 = s2.split(",")
        p2 = Point(int(x2), int(y2))
        result.append(Line(p1, p2))
    return result

def filter_lines(lines: list[Line]) -> list[Line]:
    result = []
    for line in lines:
        if line.isVertical() or line.isHorizontal():
            result.append(line)
    return result

def get_points_count(lines: list[Line]) -> dict[Point, int]:
    result = {}
    for line in lines:
        points = line.getPoints()
        for point in points:
            if point in result:
                result[point] += 1
            else:
                result[point] = 1
    return result

if __name__ == "__main__" :
    with open("input/day5.txt", "r") as f:
        data = [l for l in f ]
    
    lines = parse_lines(data)
    # h_v_lines = filter_lines(lines)
    points_count = get_points_count(lines)
    threshold = 1
    count = 0
    for point in points_count.values():
        if point > threshold:
            count += 1

    print(str(count))
