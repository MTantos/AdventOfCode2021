def parse_pairs(polymer:str) -> dict[str, int]:
    result = {}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        if pair in result:
            result[pair] += 1
        else:
            result[pair] = 1
    return result

def parse_insertions(pairs:list[str]) -> dict[str, tuple[str, str]]:
    result = {}
    for pair in pairs:
        key = pair[0:2]
        value = (pair[0]+pair[-2], pair[-2]+pair[1])
        result[key] = value
    return result

def calc_answer(pairs:dict[str,int], map:dict[str, tuple[str, str]], steps:int, last_element:str) -> None:
    for i in range(steps):
        new_pairs = {}
        for item in pairs.items():
            ps = map[item[0]]
            for p in ps:
                if p in new_pairs:
                    new_pairs[p] += item[1]
                else:
                    new_pairs[p] = item[1]
        pairs = new_pairs

    elements = {}
    for item in pairs.items():
        c = item[0][0]
        if c in elements:
            elements[c] += item[1]
        else:
            elements[c] = item[1]
    elements[last_element] += 1

    min = ('a', 0xFFFFFFFFFFFFFFFF)
    max = ('a', 0)
    for e in elements.items():
        if min[1] > e[1]:
            min = e
        if max[1] < e[1]:
            max = e
    print('Min: ' + str(min) + ", Max: " + str(max) + ", Dif: " + str(max[1]-min[1]))

if __name__ == "__main__" :
    with open("input/day14.txt", "r") as f:
        lines = [l for l in f]

    polymer = lines[0][0:-1]
    rules = lines[2:]
    pairs = parse_pairs(polymer)
    map = parse_insertions(rules)

    # Part 1
    steps = 10
    calc_answer(pairs, map, steps, polymer[-1])

    # Part 2
    steps = 40
    calc_answer(pairs, map, steps, polymer[-1])
