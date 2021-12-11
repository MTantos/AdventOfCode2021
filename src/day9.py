def is_local_low(nums:list[list[int]], i:int, j:int) -> bool:
    if (i < len(nums) - 1) and (nums[i][j] >= nums[i+1][j]):
        return False
    if (i > 0 and nums[i][j]) >= (nums[i-1][j]):
        return False
    if (j < len(nums[0])) - 1 and (nums[i][j] >= nums[i][j+1]):
        return False
    if (j > 0 and nums[i][j]) >= (nums[i][j-1]):
        return False
    return True

def get_basin_size(nums:list[list[int]], i:int, j:int) -> int:
    vals = [(i,j)]
    result = 0
    while len(vals) > 0:
        i = vals[0][0]
        j = vals[0][1]
        if nums[i][j] != 9:
            result += 1
            nums[i][j] = 9
            if i < len(nums) - 1:
                vals.append((i+1,j))
            if i > 0:
                vals.append((i-1,j))
            if j < len(nums[0]) - 1:
                vals.append((i,j+1))
            if j > 0:
                vals.append((i,j-1))
        vals.pop(0)
    return result

if __name__ == "__main__" :
    with open("input/day9.txt", "r") as f:
        lines = [l for l in f]

    nums = []
    for line in lines:
        nums.append([int(i) for i in line[:-1]])

    # Part 1
    risk = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if is_local_low(nums, i, j):
                risk += nums[i][j] + 1
    print("Risk value is: " + str(risk))

    # Part 2
    basin_sizes = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            basin_size = get_basin_size(nums, i, j)
            if basin_size:
                basin_sizes.append(basin_size)
    basin_sizes.sort(reverse=True)
    print("Product of 3 lagest basins: " + str(basin_sizes[0]*basin_sizes[1]*basin_sizes[2]))
