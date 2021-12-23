class Node(object):
    def __init__(self, l = None, r = None, v = None, p = None) -> None:
        super().__init__()
        self.l = l
        self.r = r
        self.v = v
        self.p = p
        if l:
            l.p = self
        if r:
            r.p = self
    
    def __str__(self) -> str:
        if self.is_value():
            return str(self.v)
        return "[" + str(self.l) + "," + str(self.r) + "]"

    def is_value(self) -> bool:
        return self.v != None

    def get_left_child(self):
        if self.is_value():
            return self
        return self.l.get_left_child()

    def get_right_child(self):
        if self.is_value():
            return self
        return self.r.get_right_child()
    
    def get_left(self):
        if self.p:
            if self.p.l != self:
                return self.p.l.get_right_child()
            return self.p.get_left()
        return None

    def get_right(self):
        if self.p:
            if self.p.r != self:
                return self.p.r.get_left_child()
            return self.p.get_right()
        return None

    def explode(self, h: int) -> bool:
        if self.is_value() or h < 4:
            return False
        if self.l.v == 7 and self.r.v == 7:
            None
        l = self.get_left()
        if l:
            l.v += self.l.v
        r = self.get_right()
        if r:
            r.v += self.r.v
        self.v = 0
        self.l = self.r = None
        return True

    def split(self) -> bool:
        if self.is_value() and self.v >= 10:
            self.l = Node(v=self.v>>1, p=self)
            self.r = Node(v=(self.v+1)>>1, p=self)
            self.v = None
            return True
        return False
    
    def clone(self):
        if self.is_value():
            return Node(v=self.v)
        return Node(self.l.clone(), self.r.clone())

def parse_node(line:str, i:int) -> tuple[Node,int]:
    c = line[i]
    if c == "[":
        l, i = parse_node(line, i+1)
        if line[i] != ",":
            raise Exception("Encountered: " + line[i] + ", expected ','")
        r, i = parse_node(line, i+1)
        if line[i] != "]":
            raise Exception("Encountered: " + line[i] +", expected ]")
        return Node(l, r), i+1
    if c.isdigit():
        return Node(v=int(c)), i+1
    raise Exception("Oops")

def parse_line(line:str) -> Node:
    return parse_node(line, 0)[0]

def explode_node(node:Node, h:int) -> bool:
    if node:
        return explode_node(node.l, h+1) or node.explode(h) or explode_node(node.r, h+1)
    return False    

def split_node(node: Node) -> bool:
    if node:
        return split_node(node.l) or node.split() or split_node(node.r)
    return False

def reduce_node(node:Node) -> None:
    while explode_node(node, 0) or split_node(node):
        None

def magnitude(node:Node) -> int:
    return node.v if node.is_value() else magnitude(node.l) * 3 + magnitude(node.r) * 2

if __name__ == "__main__" :
    with open("input/day18.txt", "r") as f:
        lines = [l[0:-1] for l in f]

    # Part 1
    node = parse_line(lines[0])
    reduce_node(node)
    for line in lines[1:]:
        node = Node(node, parse_line(line))
        reduce_node(node)
    print(str(node))
    print("Magnitude: " + str(magnitude(node)))

    # Part 2
    nodes = [parse_line(line) for line in lines]
    max_mag = 0
    for x in nodes:
        for y in nodes:
            if x != y:
                node = Node(x.clone(), y.clone())
                reduce_node(node)
                max_mag = max(max_mag, magnitude(node))
    print("Maximum Magnitude: " + str(max_mag))
