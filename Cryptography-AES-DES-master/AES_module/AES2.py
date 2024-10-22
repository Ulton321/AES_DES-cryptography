s_box = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

inverse_s_box = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]


RC = [
    '00000001',
    '00000010',
    '00000100',
    '00001000',
    '00010000',
    '00100000',
    '01000000',
    '10000000',
    '00011011',
    '00110110'
]


def byte_substitution_helper(byte1, byte2):
    byte_value = int(byte1 + byte2, 16)
    row = byte_value // 16
    col = byte_value % 16
    result = s_box[row][col]
    return result

def byte_substitution(byte):
    result = ""
    for i in range(0, len(byte), 2):
        byte1 = byte[i]
        byte2 = byte[i+1]
        a = byte_substitution_helper(byte1, byte2)
        result += a
    return result

def inverse_byte_substitution_helper(byte1, byte2):
    byte_value = int(byte1 + byte2, 16)
    row = byte_value // 16
    col = byte_value % 16
    result = inverse_s_box[row][col]
    return result

def inverse_byte_substitution(byte):
    result = ""
    for i in range(0, len(byte), 2):
        byte1 = byte[i]
        byte2 = byte[i+1]
        a = inverse_byte_substitution_helper(byte1, byte2)
        result += a
    return result

def string_to_matrix(input_string):
    # convert a string of bytes to a matrix as an array
    matrix = []
    for i in range(0, len(input_string), 8):
        row = []
        for j in range(4):
            row.append(input_string[i+2*j:i + 2*j + 2])
        matrix.append(row)
    return matrix # return the transposed version of the matrix

def transpose_matrix(matrix):
    return [list(x) for x in zip(*matrix)]

def matrix_to_string(matrix):
    output_string = ''
    for row in matrix:
        for char in row:
            output_string += char
    return output_string

def shift_rows(matrix):
    matrix = transpose_matrix(string_to_matrix(matrix))
    for i in range(1, 4):
        matrix[i] = matrix[i][i:] + matrix[i][:i]
    return matrix_to_string(transpose_matrix(matrix))

def inverse_shift_rows(matrix):
    matrix = transpose_matrix(string_to_matrix(matrix))
    for i in range(1, 4):
        matrix[i] = matrix[i][-i:] + matrix[i][:-i]
    return matrix_to_string(transpose_matrix(matrix))

def bin_to_hex(binary):
    hex = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'
        }
    result = ""
    for i in range(0, len(binary), 4):
        n = ""
        n = n + binary[i]
        n = n + binary[i+1]
        n = n + binary[i+2]
        n = n + binary[i+3]
        result = result + hex[n]
    return result

def hex_to_bin(hex):
    binary = {
            '0': "0000",
            '1': "0001",
            '2': "0010",
            '3': "0011",
            '4': "0100",
            '5': "0101",
            '6': "0110",
            '7': "0111",
            '8': "1000",
            '9': "1001",
            'A': "1010",
            'B': "1011",
            'C': "1100",
            'D': "1101",
            'E': "1110",
            'F': "1111"         
         }
    result = ""
    for i in hex:
        result += binary[i.upper()]
    return result

def add(A, B):
    # make sure A, B have the same length
    while len(A) > len(B):
        B = '0' + B
    while len(B) > len(A):
        A = '0' + A
    C = ''
    for i in range(len(A)):
        if A[i] == B[i]:
            C += '0'
        else:
            C+= '1'
    # Get rid of zeros in front of C
    i = 0
    while i<len(C) and C[i] == '0':
        i += 1
    if i == len(C):
        C = '0' # all 0s
    else:
        C = C[i:]
    return C

# multiplication function
# first do multiplication without mod
def multiply(A, B):
    C = '0' # result
    for i in range(len(B)-1, -1, -1):
        if B[i] == '1':
            C = add(C, A)
        A = A + '0'
    return C

def mod(A, P):
    # 101110 substr -> 10111 then add 10111 + P, then addpend it to the leftover substr
    # use substr, then add it, and then append it to the leftover substr
    result = A
    while len(result) >= len(P):
        left = add(result[:len(P)], P)
        right = result[len(P):]
        result = left + right
    return result

# matrix-multiplication for encryption
def matrix_multiplication(column):
    one = "00000001"
    two = "00000010"
    three = "00000011"
    GF = "100011011"
    MATRIX = [[two, three, one, one], [one, two, three, one], [one, one, two, three], [three, one, one, two]]

    result = []
    for i in range(4):
        total = "00000000"
        for j in range(4):
            multiplied = mod(multiply(MATRIX[i][j], column[j]), GF)
            total = add(total, multiplied)
        result.append(total)
    return result

# matrix multiplication for decryption
def inverse_matrix_multiplication(column):
    nine = "00001001"
    b = "00001011"
    d = "00001101"
    e = "00001110"
    GF = "100011011"
    MATRIX = [[e, b, d, nine], [nine, e, b, d], [d, nine, e, b], [b, d, nine, e]]

    result = []
    for i in range(4):
        total = "00000000"
        for j in range(4):
            multiplied = mod(multiply(MATRIX[i][j], column[j]), GF)
            total = add(total, multiplied)
        result.append(total)
    return result

def mix_columns(hex):
    a = string_to_matrix(hex)
    binary = []
    for i in a:
        n = []
        for j in i:
            n.append(hex_to_bin(j))
        binary.append(n)   

    result = []
    for k in binary:
        result.append(matrix_multiplication(k))
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            while len(result[i][j]) < 8:
                result[i][j] = "0" + result[i][j]
                
    return bin_to_hex(matrix_to_string(result)) 

def inverse_mix_columns(hex):
    a = string_to_matrix(hex)
    binary = []
    for i in a:
        n = []
        for j in i:
            n.append(hex_to_bin(j))
        binary.append(n)   

    result = []
    for k in binary:
        result.append(inverse_matrix_multiplication(k))
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            while len(result[i][j]) < 8:
                result[i][j] = "0" + result[i][j]
                
    return bin_to_hex(matrix_to_string(result)) 

# xor two 128-bits in hexadecimal
def xor(a, b):
    a = hex_to_bin(a)

    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    
    return bin_to_hex(result)

# g-function that will take 32-bits 
def g(key, round_constant):
    # split the 4 bytes key segment
    v0, v1, v2, v3 = key[0:2], key[2:4], key[4:6], key[6:8]

    # rotate the segments
    v0, v1, v2, v3 = v1, v2, v3, v0

    # concatenate the new bytes order
    bytes = v0  + v1 + v2 + v3

    # use s-box substitution
    result = ""
    for i in range(0, len(bytes), 2):
        byte1 = bytes[i]
        byte2 = bytes[i+1]
        a = byte_substitution_helper(byte1, byte2)
        result += a
    
    # get the first bytes of result
    sample = result[0:2]

    # xor with the RC depending on the round
    xor_sample = xor(sample, RC[round_constant])

    # concatenate the xor and replace it back to its order
    result = xor_sample + result[2:8]

    return result

def key_schedule(key):
    # split the 16 bytes into 4 blocks
    result = []
    w0, w1, w2, w3 = key[0:8], key[8:16], key[16:24], key[24:32]

    initial_key = w0 + w1 + w2 + w3
    result.append(initial_key)

    for i in range(10):
        a = xor(w0, hex_to_bin(g(w3, i)))
        b = xor(a, hex_to_bin(w1))
        c = xor(b, hex_to_bin(w2))
        d = xor(c, hex_to_bin(w3))

        new_key = a + b + c + d
        result.append(new_key)

        w0, w1, w2, w3 = new_key[:8], new_key[8:16], new_key[16:24], new_key[24:32]

    return result

def encrypt(text, key_string):
    key = key_schedule(key_string) # initialize key schedule

    # first key addition layer
    result = xor(text, hex_to_bin(key[0]))

    for i in range(1, 10):
        # byte substitution layer
        substituted_string = byte_substitution(result)
        shifted_rows = shift_rows(substituted_string)
        mixed_columns = mix_columns(shifted_rows)
        key_addition = xor(mixed_columns, hex_to_bin(key[i]))
        result = key_addition

    result = byte_substitution(result)
    result = shift_rows(result)
    result = xor(result, hex_to_bin(key[10]))

    return result

def decrypt(cipher, key_string):
    key = key_schedule(key_string)

    # first key addition layer
    result = xor(cipher, hex_to_bin(key[10]))
    result = inverse_shift_rows(result)
    result = inverse_byte_substitution(result)

    for i in range(9, 0, -1):
        key_addition = xor(result, hex_to_bin(key[i]))
        inversed_mixed_columns = inverse_mix_columns(key_addition)
        inversed_shifted_rows = inverse_shift_rows(inversed_mixed_columns)
        inversed_byte_substitution = inverse_byte_substitution(inversed_shifted_rows)
        result = inversed_byte_substitution
    
    result = xor(result, hex_to_bin(key[0]))
    
    return result

# hex_string = '00112233445566778899aabbccddeeff'
# key_string = '000102030405060708090a0b0c0d0e0f'
# substituted_string = byte_substitution(hex_string) # substitute the stringz
# shifted_rows = shift_rows(substituted_string) # shift the rows and return as string
# mixed_columns = mix_columns(shifted_rows)

# hex_string = "00000048656c6c6f2c20576f726c6421"
# key_string = "00000000000000000000000000313233"

# cipher = encrypt(hex_string, key_string)
# decipher = decrypt(cipher, key_string)

# print("Original Text: " + hex_string)
# print("Cipher Text: " + cipher)
# print("Decipher Text: " + decipher)