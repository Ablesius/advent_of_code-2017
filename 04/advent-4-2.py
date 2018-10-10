with open('puzzle_input') as puzzle_input:
    lines = []
    for line in puzzle_input.readlines():
        lines.append(line.split())
    del lines[-1]   # empty list, counts as 1 which we don't want


def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)


def get_anagram_base(string1):
    return ''.join(sorted(string1))


number_passphrases = len(lines)
number_valid_passphrases = 0

for line in lines:
    tmp_line = []
    for word in line:
        tmp_line.append(get_anagram_base(word))
    tmp_line = set(tmp_line)
    if len(tmp_line) == len(line):
        number_valid_passphrases += 1


print(number_valid_passphrases)
