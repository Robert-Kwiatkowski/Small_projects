import math
def divisorLoop(d):
    return_divisors = []
    x = math.floor(math.sqrt(d))
    if x ** 2 == d:
        return_divisors.append(x)
        return_divisors.append(x)
        return return_divisors
    else:
        x += 1

    while x < (d + 1) / 2:
        y_square = x ** 2 - d
        y = math.sqrt(y_square)
        if y_square > 0 and math.floor(y) == y:
            return_divisors.append(x + y)
            return_divisors.append(x - y)
            break
        else:
            x += 1
    return return_divisors


def fermat(number):
    d = number
    exponent = 0
    while d % 2 == 0:
        exponent += 1
        d /= 2

    divisors = {2: exponent}
    new_divisors = divisorLoop(d)
    if len(new_divisors) == 0:
        divisors.update({int(d): 1})
        return divisors

    temp_divisors = {new_divisors[0]: 1}
    if new_divisors[1] in temp_divisors:
        temp_divisors.update({new_divisors[1]: 2})
    else:
        temp_divisors.update({new_divisors[1]: 1})

    check_index = 0
    while True:
        value_to_check = list(temp_divisors.keys())[check_index]
        tmp_divisors = divisorLoop(value_to_check)
        if not tmp_divisors:
            check_index += 1
            if check_index >= len(temp_divisors):
                break
        else:
            temp_divisors.update({value_to_check: temp_divisors[value_to_check] - 1})
            if temp_divisors[value_to_check] == 0:
                check_index += 1

            for i in range(2):
                tmp_divisor = tmp_divisors[i]
                if tmp_divisor in temp_divisors:
                    temp_divisors.update({tmp_divisor: temp_divisors[tmp_divisor] + 1})
                else:
                    temp_divisors.update({tmp_divisor: 1})

    for divisor in temp_divisors:
        if temp_divisors[divisor] > 0:
            if divisor in divisors:
                divisors.update({divisor: divisors[tmp_divisor] + 1})
            else:
                divisors.update({divisor: temp_divisors[divisor]})
    return divisors

print(fermat(256))
keys = list(fermat(n - 1).keys())
