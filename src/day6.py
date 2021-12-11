if __name__ == "__main__" :
    with open("input/day6.txt", "r") as f:
        lines = [l for l in f]

    nums = lines[0].split(",") # only 1 input line
    fish = [0,0,0,0,0,0,0,0,0]
    for num in nums:
        fish[int(num)] += 1
    days = 256
    while days > 0:
        temp = fish[0]
        for i in range(1, 9):
            fish[i-1] = fish[i]
        fish[6] += temp
        fish[8] = temp
        days -= 1
    
    print("There are " + str(sum(fish)) + " fish")