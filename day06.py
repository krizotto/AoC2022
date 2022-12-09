def find_transmission_index(message, packet_length) -> int:
    for i in range(len(message) - packet_length):
        packet = message[i : i + packet_length]
        if len(set(packet)) == len(packet):
            return i + packet_length
    return -1


data = [x.strip() for x in open("data/day06.txt", "r").readline()]
print("Part 1:", find_transmission_index(data, 4))
print("Part 2:", find_transmission_index(data, 14))
