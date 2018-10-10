with open('puzzle_input') as puzzle_input:
    lines = []
    for line in puzzle_input.readlines():
        lines.append(line.split())
    del lines[-1]   # empty list, counts as 1 which we don't want


number_passphrases = len(lines)
number_valid_passphrases = 0

for line in lines:
    if len(line) == len(set(line)):
        number_valid_passphrases += 1

print(number_valid_passphrases)
