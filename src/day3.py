if __name__ == "__main__" :
    with open("input/day3.txt", "r") as f:
        lines = [l for l in f ]
    
    # Part 1
    threshold = len(lines) / 2
    bits = len(lines[0]) - 1
    counts = [0 for x in range(bits)]
    for line in lines:
        for i in range(bits):
            if line[i] == "1":
                counts[i] += 1
    gamma = 0
    mask = 0
    for i in range(bits):
        gamma <<= 1
        mask <<= 1
        if counts[i] > threshold:
            gamma += 1
        mask += 1
    epsilon = ~gamma & mask
    print("epsilon: " + str(epsilon) + ", gamma: " + str(gamma) + ", product: " + str(epsilon * gamma))

    # Part 2
    i = 0
    ogr = lines
    while len(ogr) > 1:
        zeros = []
        ones = []
        for line in ogr:
            if line[i] == "0":
                zeros.append(line)
            else:
                ones.append(line)
        if len(zeros) > len(ones):
            ogr = zeros
        else:
            ogr = ones
        i = (i + 1) % bits
    print("Oxygen Generator Rating: " + ogr[0][:-1])

    i = 0
    csr = lines
    while len(csr) > 1:
        zeros = []
        ones = []
        for line in csr:
            if line[i] == "0":
                zeros.append(line)
            else:
                ones.append(line)
        if len(zeros) <= len(ones):
            csr = zeros
        else:
            csr = ones
        i = (i + 1) % bits
    print("CO2 scrubber rating: " + csr[0][:-1])
    product = int(ogr[0], 2) * int(csr[0], 2)
    print("Product: " + str(product))