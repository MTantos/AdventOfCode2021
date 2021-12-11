if __name__ == "__main__" :
    with open("input/day7.txt", "r") as f:
        lines = [l for l in f]

    nums = [int(n) for n in lines[0].split(",")] # only 1 input line
    # Part 1
    nums.sort()
    median = nums[len(nums)//2]
    delta = 0
    for num in nums:
        delta += abs(median - num)
    print("Total fuel cost for pos " + str(median) + " is " + str(delta))
    
    # Part 2
    av = sum(nums) // len(nums)
    fuel = 0
    for num in nums:
        d = abs(av - num)
        fuel += d*(d+1)//2
    print("Total fuel cost for pos " + str(av) + " is " + str(fuel))
