if __name__ == "__main__" :
    with open("input/day1.txt", "r") as f:
        nums = [int(i) for i in f ]
    count = 0
    ma = 3
    for i in range(ma, len(nums)):
        a = nums[i-3] + nums[i-2] + nums[i-1]
        b = nums[i-2] + nums[i-1] + nums[i]
        if b > a:
            count += 1
    print(str(count))
