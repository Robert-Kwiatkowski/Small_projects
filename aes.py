import string, os, copy


def printInEqualColumns(*prt_values):
    prt_array = list(str(prt) for prt in prt_values)
    # Get spaces depending on terminal width
    spaces = os.get_terminal_size().columns // len(prt_array)
    # Get correct print string to format
    print_format_array = [('{:' + str(spaces) + '}') for i in prt_array]
    print_format = ""
    for pr_form in print_format_array:
        print_format += pr_form
    # Get correct print values
    print_array = prt_array
    for prt_value in print_array:
        if len(str(prt_value)) > spaces:
            index = print_array.index(prt_value)
            print_array[index] = str(prt_value)[:spaces - 5] + '...'
    # Print
    print((print_format).format(*prt_array))


def printMatrix(matrix):
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            print(f"{col}{row}: {matrix[col][row]}")


def isHex(stringToCheck):
    return set(stringToCheck).issubset(string.hexdigits)


def getHex(value, precision):
    return ('{:0' + str(precision) + 'x}').format(value)


def getBin(value, precision):
    return ('{:0' + str(precision) + 'b}').format(value)


def getBinArray(value, precision):
    return [int(x) for x in list(getBin(value, precision))]


def getBinStringFromArray(bin_array):
    bin_string = ""
    for bin_digit in bin_array:
        bin_string += str(bin_digit)
    return bin_string


def getBinMatrix(value):
    bin_array = getBinArray(value, 16)
    bin_cell = []
    bin_row = []
    bin_matrix = [-1, -1]
    row = 0
    for bin_digit in bin_array:
        bin_cell.append(bin_digit)
        if len(bin_cell) == 4:
            bin_row.append(bin_cell)
            bin_cell = []
            if len(bin_row) == 2:
                bin_matrix[row] = bin_row
                bin_row = []
                row += 1
    return bin_matrix


def getBinArrayDecValue(bin_array):
    bin_string = ""
    for bin_value in bin_array:
        bin_string += str(bin_value)
    return int(bin_string, 2)


def getBinMatrixDecValue(bin_matrix):
    bin_string = ""
    for bin_row in bin_matrix:
        for bin_cell in bin_row:
            bin_string += getBinStringFromArray(bin_cell)
    return int(bin_string, 2)


def getCorrectHexText(prompt):
    text = ""
    while True:
        text = input(prompt).lower()
        if isHex(text):
            break
        print("Try again")
    if len(text) % 4 is not 0:
        text += "".join("0" for x in range(4 - len(text) % 4))  # add 0 on the end
    return text


def removeUnnecessaryNumbersInBinArray(bin_array):
    new_bin_array = bin_array.copy()
    bin_string = getBinStringFromArray(bin_array)
    while True:
        if new_bin_array[0] == 0:
            new_bin_array.pop(0)
            if (len(new_bin_array) == 0):
                break
        else:
            break
    return new_bin_array


def xorTwoBinArrays(bin_array1, bin_array2):
    return [(x + y) % 2 for x, y in zip(bin_array1, bin_array2)]


def sumOfTwoBinMatrixes(bin_matrix1, bin_matrix2):
    bin_matrix_sum = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            bin_matrix_sum[i][j] = xorTwoBinArrays(bin_matrix1[i][j], bin_matrix2[i][j])
    return bin_matrix_sum


def divOfTwoBinArrays(dividend, divisor):
    quotient_bin_array = [0 for x in range(len(dividend))]
    current_dividend = dividend
    dividend_power = len(current_dividend)
    divisor_power = len(divisor)
    power_diff = dividend_power - divisor_power

    while (power_diff >= 0):
        div_position = dividend_power - power_diff - 1
        quotient_bin_array[div_position] = 1

        temp_div = (divisor + [0 for x in range(power_diff)])
        current_dividend = xorTwoBinArrays(current_dividend, temp_div)
        current_dividend = removeUnnecessaryNumbersInBinArray(current_dividend)
        power_diff = len(current_dividend) - divisor_power

    quotient_bin_array = removeUnnecessaryNumbersInBinArray(quotient_bin_array)
    remainder_bin_array = (getBinArray(getBinArrayDecValue(current_dividend), 4)
                           if current_dividend
                           else [0, 0, 0, 0])

    return quotient_bin_array, remainder_bin_array


def mulOfTwoBinArrays(bin_array1, bin_array2):
    mul_bin_array = [0 for x in range(len(bin_array1 + bin_array2) - 1)]
    for i in range(len(bin_array1)):
        for j in range(len(bin_array2)):
            mul_bin_array[i + j] += bin_array1[i] * bin_array2[j]
    return [x % 2 for x in mul_bin_array]


def iloczyn_bin_matrix(bin_matrix1, bin_matrix2):
    bin_matrix_mul = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            prev_result = []
            for k in range(2):
                mul_result = mulOfTwoBinArrays(bin_matrix1[i][k], bin_matrix2[k][j])
                x, remainder_bin_array = divOfTwoBinArrays(mul_result, reduction_polynomial)
                if k == 0:
                    prev_result = remainder_bin_array
            bin_matrix_mul[i][j] = xorTwoBinArrays(remainder_bin_array, prev_result)
    return bin_matrix_mul


# GLOBAL VARIABLES

sbox_E = {
    '0': 'e', '1': '4', '2': 'd', '3': '1', '4': '2', '5': 'f', '6': 'b', '7': '8',
    '8': '3', '9': 'a', 'a': '6', 'b': 'c', 'c': '5', 'd': '9', 'e': '0', 'f': '7'
}
sbox_D = {
    '0': 'e', '1': '3', '2': '4', '3': '8', '4': '1', '5': 'e', '6': 'a', '7': 'f',
    '8': '7', '9': 'd', 'a': '9', 'b': '6', 'c': 'b', 'd': '2', 'e': '0', 'f': '5'
}
reduction_polynomial = [1, 0, 0, 1, 1]


# Głowne funkcje

def ZK(bin_matrix):
    bin_matrix_result = copy.deepcopy(bin_matrix)
    bin_matrix_result[1][0], bin_matrix_result[1][1] = bin_matrix_result[1][1], bin_matrix_result[1][0]
    return bin_matrix_result


def sbox(bin_array, sbox_dict):
    bin_string = getBinStringFromArray(bin_array)
    bin_array_hex_value = getHex(int(bin_string, 2), 0)
    return getBinArray(int(sbox_dict[bin_array_hex_value], 16), 4)


def sboxMatrix(bin_matrix, sbox_dict):
    bin_matrix_result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            bin_matrix_result[i][j] = sbox(bin_matrix[i][j], sbox_dict)
    return bin_matrix_result


def getKeys(key_start):
    k1 = [[0, 0], [0, 0]]
    k1[0][0] = xorTwoBinArrays(key_start[0][0], sbox(key_start[1][1], sbox_E))
    k1[0][0] = xorTwoBinArrays(k1[0][0], [0, 0, 0, 1])
    k1[1][0] = xorTwoBinArrays(key_start[1][0], k1[0][0])
    k1[0][1] = xorTwoBinArrays(key_start[0][1], k1[1][0])
    k1[1][1] = xorTwoBinArrays(key_start[1][1], k1[0][1])
    k2 = [[0, 0], [0, 0]]
    k2[0][0] = xorTwoBinArrays(k1[0][0], sbox(k1[1][1], sbox_E))
    k2[0][0] = xorTwoBinArrays(k2[0][0], [0, 0, 1, 0])
    k2[1][0] = xorTwoBinArrays(k1[1][0], k2[0][0])
    k2[0][1] = xorTwoBinArrays(k1[0][1], k2[1][0])
    k2[1][1] = xorTwoBinArrays(k1[1][1], k2[0][1])
    return k1, k2


def encrypt(text_hex, key_start):
    m = [[[0, 0, 1, 1], [0, 0, 1, 0]], [[0, 0, 1, 0], [0, 0, 1, 1]]]
    print(f"Wpisano:\nText = {text_hex} \n"
          f"Key = {key_start} ")
    key_bin_matrix = getBinMatrix(int(key_start, 16))
    text_bin_matrix = getBinMatrix(int(text_hex, 16))
    k1, k2 = getKeys(key_bin_matrix)
    print(f"K1 = {getHex(getBinMatrixDecValue(k1), 4)}\n"
          f"K2 =  {getHex(getBinMatrixDecValue(k2), 4)}")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], key_bin_matrix[i][j])
    print(f"1.: ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = sboxMatrix(text_bin_matrix, sbox_E)
    print(f"2.:  ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = ZK(text_bin_matrix)
    print(f"3.:  ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = iloczyn_bin_matrix(m, text_bin_matrix)
    print(f"4.: ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], k1[i][j])
    print(f"5.:  ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = sboxMatrix(text_bin_matrix, sbox_E)
    print(f"6.: ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = ZK(text_bin_matrix)
    print(f"7.:  ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], k2[i][j])
    print(f"8.:  ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    return getHex(getBinMatrixDecValue(text_bin_matrix), 4)


def decrypt(text_hex="3CC3", key_start="3CC3"):
    m = [[[0, 0, 1, 1], [0, 0, 1, 0]], [[0, 0, 1, 0], [0, 0, 1, 1]]]
    print(f"Encrypted:\nText = {text_hex} ({int(text_hex, 16)})\nKey = {key_start} ({int(key_start, 16)})")
    key_bin_matrix = getBinMatrix(int(key_start, 16))
    text_bin_matrix = getBinMatrix(int(text_hex, 16))
    k1, k2 = getKeys(key_bin_matrix)
    print(f"K1 = {k1} ({getHex(getBinMatrixDecValue(k1), 4)})\nK2 = {k2} ({getHex(getBinMatrixDecValue(k2), 4)})")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], k2[i][j])
    print(f"1.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = ZK(text_bin_matrix)
    print(f"2.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = sboxMatrix(text_bin_matrix, sbox_D)
    print(f"3.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], k1[i][j])
    print(f"4.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = iloczyn_bin_matrix(m, text_bin_matrix)
    print(f"5.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = ZK(text_bin_matrix)
    print(f"6.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    text_bin_matrix = sboxMatrix(text_bin_matrix, sbox_D)
    print(f"7.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    for i in range(2):
        for j in range(2):
            text_bin_matrix[i][j] = xorTwoBinArrays(text_bin_matrix[i][j], key_bin_matrix[i][j])
    print(f"8.: {text_bin_matrix} ({getHex(getBinMatrixDecValue(text_bin_matrix), 4)})")
    return getHex(getBinMatrixDecValue(text_bin_matrix), 4)


# def encryptVector(text_hex, key_hex):
#     temp_txt = ""
#     temp_key = ""
#     return_string = ""
#     for chr_txt, chr_key in zip(text_hex, key_hex):
#         temp_txt += chr_txt
#         temp_key += chr_key
#         if len(temp_txt) == 4:
#             text_encrypted = encrypt(temp_txt, temp_key)
#             return_string += text_encrypted
#             temp_txt = ""
#             temp_key = ""
#     return return_string

def encryptVector(text_hex, key_hex):
    temp_txt = ""
    temp_key = ""
    return_string = ""
    for chr_txt in text_hex:
        temp_txt += chr_txt
        if len(temp_txt) == 4:
            text_encrypted = encrypt(temp_txt, key_hex)
            return_string += text_encrypted
            temp_txt = ""
            temp_key = ""
    return return_string


def decryptVector(text_hex, key_hex):
    temp_txt = ""
    temp_key = ""
    return_string = ""
    for chr_txt, chr_key in zip(text_hex, key_hex):
        temp_txt += chr_txt
        temp_key += chr_key
        if len(temp_txt) == 4:
            text_encrypted = decrypt(temp_txt, temp_key)
            return_string += text_encrypted
            temp_txt = ""
            temp_key = ""
    return return_string


# czesc glowna funkcji

text = getCorrectHexText("Wpisz tekst (hex) ")
key = getCorrectHexText("Wpisz klucz (hex) ")
text_encrypted = encryptVector(text, key)
print(f"Wynik szyfrowania to: {text_encrypted}\n\n")



"""
text_decrypted = decryptVector(text_encrypted, key)
"""