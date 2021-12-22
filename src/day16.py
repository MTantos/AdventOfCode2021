from math import prod

def hex_to_bin(s: str) -> str:
    if s == "0":
        return "0000"
    if s == "1":
        return "0001"
    if s == "2":
        return "0010"
    if s == "3":
        return "0011"
    if s == "4":
        return "0100"
    if s == "5":
        return "0101"
    if s == "6":
        return "0110"
    if s == "7":
        return "0111"
    if s == "8":
        return "1000"
    if s == "9":
        return "1001"
    if s == "A":
        return "1010"
    if s == "B":
        return "1011"
    if s == "C":
        return "1100"
    if s == "D":
        return "1101"
    if s == "E":
        return "1110"
    if s == "F":
        return "1111"

class Packet(object):
    def __init__(self, version: int, type_id: int) -> None:
        super().__init__()
        self.version = version
        self.type_id = type_id
        self.packets = []
        self.val = 0

    def add_packet(self, packet) -> None:
        self.packets.append(packet)

def parse_packet(input: str, i: int) -> tuple[Packet, int]:
    v = int(input[i:i+3], 2)
    t = int(input[i+3:i+6], 2)
    i += 6
    p = Packet(v, t)
    if t == 4:
        prefix = "1"
        s = ""
        while prefix == "1":
            prefix = input[i]
            s += input[i+1:i+5]
            i += 5
        p.val = int(s, 2)
    else:
        t_id = input[i]
        i += 1
        if t_id == "0":
            i += 15
            end = i + int(input[i-15:i], 2)
            while i < end:
                packet, i = parse_packet(input, i)
                p.add_packet(packet)
        else:
            num_packets = int(input[i:i+11], 2)
            i += 11
            for j in range(num_packets):
                packet, i = parse_packet(input, i)
                p.add_packet(packet)
    return p, i

def sum_version(packet: Packet) -> int:
    result = packet.version
    for p in packet.packets:
        result += sum_version(p)
    return result

def eval_packet(packet: Packet) -> int:
    result = 0
    if packet.type_id == 0:
        result = sum(eval_packet(p) for p in packet.packets)
    elif packet.type_id == 1:
        result = prod(eval_packet(p) for p in packet.packets)
    elif packet.type_id == 2:
        result = min(eval_packet(p) for p in packet.packets)
    elif packet.type_id == 3:
        result = max(eval_packet(p) for p in packet.packets)
    elif packet.type_id == 4:
        result = packet.val
    elif packet.type_id == 5:
        result = 1 if eval_packet(packet.packets[0]) > eval_packet(packet.packets[1]) else 0
    elif packet.type_id == 6:
        result = 1 if eval_packet(packet.packets[0]) < eval_packet(packet.packets[1]) else 0
    elif packet.type_id == 7:
        result = 1 if eval_packet(packet.packets[0]) == eval_packet(packet.packets[1]) else 0
    return result

if __name__ == "__main__" :
    with open("input/day16.txt", "r") as f:
        lines = [l[0:-1] for l in f]
    hex = lines[0]

    bin = ""
    for c in hex:
        bin += hex_to_bin(c)
    packet, _ = parse_packet(bin, 0)

    # Part 1
    v_sum = sum_version(packet)
    print("version sum: " + str(v_sum))

    # Part 2
    val = eval_packet(packet)
    print("outermost packet value: " + str(val))
