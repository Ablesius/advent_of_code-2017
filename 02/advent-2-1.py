# test_matrix_line = '123 4 12 23 5'
# test = test_matrix_line.split()
# test
# test.max()
# max(test)
# test_ = []
# for i in test:
#         test_.append(int(i))


def get_checksum(line):
    return max(line) - min(line)


with open('advent-2_input') as puzzle_input:
    lines = puzzle_input.readlines()

rows = []
summa = 0
for line in lines:
    line = line.rstrip().split()
    new_line = []
    for i in line:
        new_line.append(int(i))
    summa += get_checksum(new_line)


if __name__ == '__main__':
    print(summa)
