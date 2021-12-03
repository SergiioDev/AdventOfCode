def day_two(file):
    f = open(file, 'r')
    horizontal = aim = depth = 0
    for x in f.readlines():
        current_line = x.split(' ', 1)
        current_number = int(current_line[1])

        if "forward" in current_line:
            horizontal += current_number
            depth += aim * current_number

        if "down" in current_line:
            aim += current_number

        if "up" in current_line:
            aim -= current_number

    return horizontal * depth


print(day_two("DayTwo/day_two.txt"))
