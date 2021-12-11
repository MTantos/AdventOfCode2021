def get_b(segments:dict[str,int]) -> str:
    for segment in segments.items():
        if segment[1] == 6:
            return segment[0]

def get_e(segments:dict[str,int]) -> str:
    for segment in segments.items():
        if segment[1] == 4:
            return segment[0]

def get_c(segments:dict[str,int], seg:str) -> str:
    for segment in segments.items():
        if segment[1] == 8 and seg.__contains__(segment[0]):
            return segment[0]

if __name__ == "__main__" :
    with open("input/day8.txt", "r") as f:
        lines = [l for l in f]

    # Part 1
    outputs = []
    for line in lines:
        i,o = line[:-1].split(" | ")
        outputs += o.split(" ")

    count = 0
    for o in outputs:
        length = len(o)
        if length == 2 or length == 3 or length == 4 or length == 7:
            count += 1
    print("1, 4, 7, or 8 appear " + str(count) + " times")

    # Part 2
    total = 0
    for line in lines:
        i,o = line[:-1].split(" | ")
        segments = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
        for seg in i:
            if seg != " ":
                segments[seg] += 1
        for seg in i.split(" "):
            if len(seg) == 2:
                one = seg
        output = 0
        for display in o.split(" "):
            output *= 10
            seg_count = len(display)
            if seg_count == 2: # 1
                output += 1
            elif seg_count == 3: # 7
                output += 7
            elif seg_count == 4: # 4
                output += 4
            elif seg_count == 5: # 2, 3 on 5
                b = get_b(segments)
                e = get_e(segments)
                if display.__contains__(b):
                    output += 5
                elif display.__contains__(e):
                    output += 2
                else:
                    output += 3
            elif seg_count == 6: # 0, 6 or 9
                e = get_e(segments)
                c = get_c(segments, one)
                if not display.__contains__(e):
                    output += 9
                elif not display.__contains__(c):
                    output += 6
                else:
                    output += 0
            else: # 8
                output += 8
        total += output
    print("Total of all displays: " + str(total))
