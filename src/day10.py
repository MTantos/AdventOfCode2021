CLOSE_PAIRS = {")":"(","]":"[","}":"{",">":"<"}
CLOSE_SCORES = {")":3,"]":57,"}":1197,">":25137}

OPEN_PAIRS = {"(":")","[":"]","{":"}","<":">"}
OPEN_SCORES = {"(":1,"[":2,"{":3,"<":4}

def get_score(line:str) -> int:
    input = []
    for c in line:
        expected = CLOSE_PAIRS.get(c)
        if expected:
            if expected != input.pop():
                return CLOSE_SCORES.get(c)
        else:
            input.append(c)
    return 0

def get_i_score(line:str) -> int:
    input = []
    for c in line[:-1]:
        if c in OPEN_PAIRS:
            input.append(c)
        else:
            input.pop()
    score = 0
    input.reverse()
    for c in input:
        score *= 5
        score += OPEN_SCORES[c]
    return score

if __name__ == "__main__" :
    with open("input/day10.txt", "r") as f:
        lines = [l for l in f]

    error_score = 0
    incomplete_scores = []
    for line in lines:
        e_score = get_score(line)
        error_score += e_score
        if not e_score:
            incomplete_scores.append(get_i_score(line))
    incomplete_scores.sort()
    middle_score = incomplete_scores[len(incomplete_scores)//2]
    print("Error Score: " + str(error_score))
    print("Middle Score: " + str(middle_score))
