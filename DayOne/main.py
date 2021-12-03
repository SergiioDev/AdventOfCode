def day_one(file):
    f = open(file, 'r')
    increased = 0
    antNumb = int(f.readline())

    for x in f.readlines():
        if int(x) > antNumb:
            increased += 1
        if int(x) != antNumb or int(x) == antNumb:
            antNumb = int(x)

    return increased


def day_one_two(file):
    f = open(file, 'r')
    antSum = 0
    numbers = []
    increased = 0
    sum = 0
    pos = 0
    count = 0

    k = f.readlines()
    for i in k:

        while count < 3 and pos < (len(k)-3):
                nu = int(k[pos + count])
                numbers.append(nu)
                count += 1

        if len(numbers)>0:

            sum = numbers[0] + numbers[1] + numbers[2]

        if sum > antSum:
            increased += 1

        if sum != antSum:
            antSum = sum

        count = 0
        pos += 1
        numbers = []

    return increased


if __name__ == '__main__':
    print(day_one_two("DayOne/day_one.txt"))
