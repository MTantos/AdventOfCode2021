class Board(object):
    def __init__(self, lines:list[str]) -> None:
        super().__init__()
        self.nums = []
        self.marks = []
        for line in lines:
            row = [int(x) for x in line.split(" ") if x]
            self.nums.append(row)
            self.marks.append([False for x in range(len(row))])

    def setNumber(self, num: int):
        for r in range(len(self.nums)):
            for c in range(len(self.nums[0])):
                if self.nums[r][c] == num:
                    self.marks[r][c] = True

    def isWinning(self):
        # Check Rows
        for row in self.marks:
            if all(row):
                return True
        # Check Cols
        for c in range(len(self.marks[0])):
            for r in range(len(self.marks)):
                if not self.marks[r][c]:
                    break
                elif self.marks[r][c] and r == (len(self.marks) - 1):
                    return True
        return False

    def getScore(self):
        score = 0
        for r in range(len(self.marks)):
            for c in range(len(self.marks[0])):
                if not self.marks[r][c]:
                    score += int(self.nums[r][c])
        return score

def parse_boards(lines):
    x = []
    boards = []
    for line in lines:
        if line == "\n":
            boards.append(Board(x))
            x.clear()
        else:
            x.append(line[:-1])
    return boards

def get_winner(nums:list[int], boards:list[Board]):
    for num in nums:
        for board in boards:
            board.setNumber(num)
            if board.isWinning():
                score = board.getScore()
                return score * num
    return 0

def get_loser(nums:list[int], boards:list[Board]):
    for num in nums:
        for board in boards.copy():
            board.setNumber(num)
            if board.isWinning():
                boards.remove(board)
        if len(boards) == 1:
            return get_winner(nums, boards)
    return 0
    
if __name__ == "__main__" :
    with open("input/day4.txt", "r") as f:
        lines = [l for l in f ]

    nums = [int(x) for x in lines[0].split(",")]
    boards = parse_boards(lines[2:])
    score = get_loser(nums, boards)
    print("Score: " + str(score))
