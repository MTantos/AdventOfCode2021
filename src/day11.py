def increase_power(nums:list[list[int]], i:int, j:int) -> None:
    nums[i][j] += 1
    if nums[i][j] == 10:
        return flash(nums, i, j)

def flash(nums:list[list[int]], i:int, j:int) -> None:
    i1 = max(i-1, 0)
    i2 = min(i+2, len(nums))
    j1 = max(j-1, 0)
    j2 = min(j+2, len(nums[0]))
    for i in range(i1,i2):
        for j in range(j1,j2):
            increase_power(nums, i, j)

def reset_octopus(nums:list[list[int]]) -> int:
    flashes = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] > 9:
                nums[i][j] = 0
                flashes += 1
    return flashes

if __name__ == "__main__" :
    with open("input/day11.txt", "r") as f:
        lines = [l for l in f]

    nums = []
    for line in lines:
        nums.append([int(c) for c in line[:-1]])

    # Part 1
    total_steps = 100
    flash_count = 0
    for step in range(total_steps):
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                increase_power(nums, i, j)
        flash_count += reset_octopus(nums)
    print(str(flash_count) + " flashes after " + str(total_steps) + " steps")

    # Part 2
    all = len(nums) * len(nums[0])
    step = 0
    while reset_octopus(nums) != all:
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                increase_power(nums, i, j)
        step += 1
    print("All octopuses flash on step " + str(step + total_steps))
