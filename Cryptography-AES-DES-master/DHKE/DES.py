import DES_utils

# initialize all the permuations, shift tables and sboxes
IP = DES_utils.IP
EP = DES_utils.EP
PF = DES_utils.PF
FP = DES_utils.FP
PC_1 = DES_utils.PC_1
PC_2 = DES_utils.PC_2
shift_table_encryption = DES_utils.shift_table_encryption
s_box = DES_utils.s_box

# util functions
binary_to_hexadecimal = DES_utils.binary_to_hexadecimal
binary_to_decimal = DES_utils.binary_to_decimal
decimal_to_binary = DES_utils.decimal_to_binary
xor = DES_utils.xor
ROL = DES_utils.ROL
permute = DES_utils.permute

# generate key schedule for key encryption
def key_schedule(key):
    # split the bits in halve
    left = key[0:28]
    right = key[28:56]
    round_key = []

    for i in range(0, 16):
        # shift the bits by n shifts by checking from the shift table
        left_key = ROL(left, shift_table_encryption[i])
        right_key = ROL(right, shift_table_encryption[i])
    
        # combine the left and right shifted keys
        combined_keys = left_key + right_key	

        #PC-2 permutate the bits
        result = permute(combined_keys, PC_2, 48)

        # create a array to store key for each rounds
        round_key.append(result)
    
    return round_key

def pad_key(key):
    while len(key) < 64:
        key += '0'
    return key[:64]

# encrypt text using DES algorithm 
def encrypt(bits, key):
    # initial permutate the bits
    bits = permute(bits, IP, 64)

    # split the bits in halves
    left = bits[0:32]
    right = bits[32:64]

    # PC-1 permutate the bits
    key = pad_key(key)
    key = permute(key, PC_1, 56)

    for i in range(0, 16):
        # expand permuation 
        right_EP = permute(right, EP, 48)

        # XOR round keys and expanded right key
        xor_key = xor(right_EP, key_schedule(key)[i])

        # use S-Boxes
        sbox_s = ""
        for j in range(0, 8):
            row = binary_to_decimal(int(xor_key[j*6] + xor_key[j*6+5]))
            column = binary_to_decimal(int(xor_key[j*6+1] + xor_key[j*6+2] + xor_key[j*6+3] + xor_key[j*6+4])) 
            value = s_box[j][row][column]
            sbox_s = sbox_s + decimal_to_binary(value)
        
        # permute within the f function
        sbox_s = permute(sbox_s, PF, 32)

        # xor the left and sbox_s
        result = xor(left, sbox_s)
        left = result

        if i != 15:
            left, right = right, left

    # concatenate final left and right    
    encrypted = left + right

    # permute with final permutation
    encrypted_text = permute(encrypted, FP, 64)
    return encrypted_text

# decrypt text using DES algorithm 
def decrypt(bits, key):
    # initial permutate the bits
    bits = permute(bits, IP, 64)

    # split the bits in halves
    left = bits[0:32]
    right = bits[32:64]

    # PC-1 permutate the bits
    key = pad_key(key)
    key = permute(key, PC_1, 56)

    key_schedule_decryption = key_schedule(key)[::-1]

    for i in range(0, 16):
        # expand permuation 
        right_EP = permute(right, EP, 48)

        # XOR round keys and expanded right key
        xor_key = xor(right_EP, key_schedule_decryption[i])

        # use S-Boxes
        sbox_s = ""
        for j in range(0, 8):
            row = binary_to_decimal(int(xor_key[j*6] + xor_key[j*6+5]))
            column = binary_to_decimal(int(xor_key[j*6+1] + xor_key[j*6+2] + xor_key[j*6+3] + xor_key[j*6+4])) 
            value = s_box[j][row][column]
            sbox_s = sbox_s + decimal_to_binary(value)
        
        # permute within the f function
        sbox_s = permute(sbox_s, PF, 32)

        # xor the left and sbox_s
        result = xor(left, sbox_s)
        left = result

        if i != 15:
            left, right = right, left

    # concatenate final left and right    
    decrypted = left + right

    # permute with final permutation
    decrypted_text = permute(decrypted, FP, 64)
    return decrypted_text