def unique_chars(line):
    return all([line[j] not in line[:j] + line[j + 1:] for j in range(len(line))])


if __name__ == "__main__":
    file = open('input.txt', 'r')
    line = file.readline()
    flag_packet = True
    flag_message = True
    for i in range(len(line)):
        packet = line[i:i + 4]
        message = line[i:i + 14]
        if unique_chars(packet) and flag_packet:
            print(i + 4)
            flag_packet = False
        elif unique_chars(message) and flag_message:
            print(i + 14)
            flag_message = False
        if not flag_packet and not flag_message:
            break
