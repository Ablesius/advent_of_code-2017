with open('puzzle_input') as puzzle_input:
    jump_instructions = puzzle_input.readlines()

# jump_instructions = [0, 0, 0, 2, -1, 3]

steps = 0
position = 0

while 0 <= position < len(jump_instructions):
    # read instruction
    instruction = int(jump_instructions[position])
    # save old instruction index
    old_position = position
    # move the appropriate amount
    position += instruction
    # increase steps by 1
    steps += 1
    jump_instructions[old_position] = int(jump_instructions[old_position]) + 1


if __name__ == '__main__':
    print(steps)
