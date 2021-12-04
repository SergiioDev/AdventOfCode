def day_three(file):
    with open(file) as f:
        data = f.readlines()
        gamma_rate = ""
        epsilon_rate = ""

        for i in range(len(data[0])):
            ones = sum(data[j][i] == "1" for j in range(len(data)))
            zeros = sum(data[j][i] == "0" for j in range(len(data)))

            if ones > zeros:
                gamma_rate += "1"
                epsilon_rate += "0"

            if zeros > ones:
                gamma_rate += "0"
                epsilon_rate += "1"

        return int(gamma_rate, 2) * int(epsilon_rate, 2)


def day_three_two(file):
    with open(file) as f:
        data = f.readlines()
        numbers = data
        oxygen = 0
        CO2 = 0
        index = 0

        while index < len(numbers[0]):
            ones = sum(numbers[j][index] == "1" for j in range(len(numbers)))
            zeros = sum(numbers[j][index] == "0" for j in range(len(numbers)))
            list = []

            if ones > zeros or ones == zeros:
                search = "1"
            else:
                search = "0"

            for k in range(len(numbers)):
                if numbers[k][index] == search:
                    list.append(numbers[k])

            if len(list) > 1:
                numbers = list
            else:
                numbers = str(list[0])
                oxygen = int(numbers, 2)
            index += 1

        numbers = data
        index = 0

        while index < len(numbers[0]):
            ones = sum(numbers[j][index] == "1" for j in range(len(numbers)))
            zeros = sum(numbers[j][index] == "0" for j in range(len(numbers)))
            list = []

            if ones > zeros or zeros == ones:
                search = "0"
            else:
                search = "1"

            for k in range(len(numbers)):
                if numbers[k][index] == search:
                    list.append(numbers[k])

            if len(list) > 1:
                numbers = list
            else:
                numbers = str(list[0])
                CO2 = int(numbers, 2)
            index += 1

        return oxygen * CO2


print(day_three("day_three.txt"))
