if __name__ == "__main__" :
    with open("input/day2.txt", "r") as f:
        lines = [l for l in f ]
    
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        direction, amount = line.split(" ")
        x = int(amount)
        if direction == "forward":
            horizontal += x
            depth += aim * x
        elif direction == "down":
            aim += x
        elif direction == "up":
            aim -= x
    print("Horizontal: " + str(horizontal) + ", Depth: " + str(depth) + ", Product: " + str(horizontal*depth))
