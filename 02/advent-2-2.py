def get_checksum(line):
    return max(line) - min(line)


with open('advent-2_input') as puzzle_input:
    lines = puzzle_input.readlines()

summa = 0
rows = []
for line in lines:
    new_line = []
    line = line.rstrip().split()
    for i in line:
        new_line.append(int(i))
    rows.append(new_line)

for row in rows:
    for i in row:
        for next_i in row:
            if not i == next_i:
                if i % next_i == 0:
                    summa += int(i/next_i)


if __name__ == '__main__':
    print(summa)
