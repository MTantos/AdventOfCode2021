def calc_min_x_vel(min_x: int) -> int:
    i = 0
    while min_x >= 0:
        i += 1
        min_x -= i
    return i

def calc_max_y_vel(min_y: int) -> int:
    return -min_y-1

def calc_height(vy: int) -> int:
    return ((vy+1)*vy)//2

def next_x_vel(x_vel: int, min_x: int, max_x: int) -> tuple[int,int]:
    t = 0
    while x_vel < max_x:
        t = 1
        x_vel += 1
        x_pos = x_vel
        while x_pos <= max_x:
            if x_pos >= min_x:
                return x_vel, t
            t += 1
            x_pos += x_vel
    return x_vel, t

def check(vx:int, vy:int, min_x:int, max_x:int, min_y:int, max_y:int) -> int:
    x, y = vx, vy
    while x <= max_x and y >= min_y:
        if x >= min_x and y <= max_y:
            return 1
        if vx > 0:
            vx -= 1
        vy -= 1
        x += vx
        y += vy
    return 0

if __name__ == "__main__" :
    with open("input/day17.txt", "r") as f:
        lines = [l[0:-1] for l in f]
    _, vals = lines[0].split(": ")
    x_range, y_range = vals.split(", ")
    min_x, max_x = [int(i) for i in x_range[2:].split("..")]
    min_y, max_y = [int(i) for i in y_range[2:].split("..")]

    # Part 1
    x_vel = calc_min_x_vel(min_x)
    y_vel = calc_max_y_vel(min_y)
    height = calc_height(y_vel)

    print("x veloctiy: " + str(x_vel))
    print("y veloctiy: " + str(y_vel))
    print("height: " + str(height))

    # Part 2
    vx_min = x_vel
    vx_max = max_x
    vy_min = min_y
    vy_max = y_vel
    count = 0
    for vx in range(vx_min, vx_max+1):
        for vy in range(vy_min, vy_max+1):
            count += check(vx, vy, min_x, max_x, min_y, max_y)
    print("Distinct velocity values: " + str(count))
