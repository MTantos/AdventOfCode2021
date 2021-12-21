class Point(object):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return self.y << 16 | self.x

    def __eq__(self, obj: object) -> bool:
        return obj.x == self.x and obj.y == self.y

    def __lt__(self, other:object) -> bool:
        return (self.y < other.y) or ((self.y == other.y) and (self.x < other.x))

class Fold(object):
    def __init__(self, dir: str, pos: int) -> None:
        super().__init__()
        self.is_horizontal = dir == 'y'
        self.pos = pos

if __name__ == "__main__" :
    with open("input/day13.txt", "r") as f:
        lines = [l for l in f]

    dots = set()
    i = 0
    line = lines[i]
    while line != '\n':
        x1, y1 = line.split(",")
        p1 = Point(int(x1), int(y1))
        dots.add(p1)
        i += 1
        line = lines[i]
        if i == 865:
            x = 1

    folds = []
    for line in lines[i+1:]:
        s1, l = line.split('=')
        folds.append(Fold(s1[-1], int(l)))

    for fold in folds:
        if fold.is_horizontal:
            for dot in dots.copy():
                if dot.y == fold.pos:
                    dots.remove(dot)
                elif dot.y > fold.pos:
                    dots.remove(dot)
                    new_dot = Point(dot.x, fold.pos + fold.pos - dot.y)
                    dots.add(new_dot)
        else:
            for dot in dots.copy():
                if dot.x == fold.pos:
                    dots.remove(dot)
                elif dot.x > fold.pos:
                    dots.remove(dot)
                    new_dot = Point(fold.pos + fold.pos - dot.x, dot.y)
                    dots.add(new_dot)

    x = y = 0
    for dot in sorted(dots):
        while y < dot.y:
            y = dot.y
            x = 0
            print()
        while x < dot.x:
            print(".", end="")
            x += 1
        x += 1
        print("#", end="")
