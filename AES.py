import string

inv_mix_col_matrix = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]
s_box = {'00': '63', '01': '7C', '02': '77', '03': '7B', '04': 'F2', '05': '6B', '06': '6F', '07': 'C5', '08': '30',
         '09': '01', '0A': '67', '0B': '2B', '0C': 'FE', '0D': 'D7', '0E': 'AB', '0F': '76', '10': 'CA', '11': '82',
         '12': 'C9', '13': '7D', '14': 'FA', '15': '59', '16': '47', '17': 'F0', '18': 'AD', '19': 'D4', '1A': 'A2',
         '1B': 'AF', '1C': '9C', '1D': 'A4', '1E': '72', '1F': 'C0', '20': 'B7', '21': 'FD', '22': '93', '23': '26',
         '24': '36', '25': '3F', '26': 'F7', '27': 'CC', '28': '34', '29': 'A5', '2A': 'E5', '2B': 'F1', '2C': '71',
         '2D': 'D8', '2E': '31', '2F': '15', '30': '04', '31': 'C7', '32': '23', '33': 'C3', '34': '18', '35': '96',
         '36': '05', '37': '9A', '38': '07', '39': '12', '3A': '80', '3B': 'E2', '3C': 'EB', '3D': '27', '3E': 'B2',
         '3F': '75', '40': '09', '41': '83', '42': '2C', '43': '1A', '44': '1B', '45': '6E', '46': '5A', '47': 'A0',
         '48': '52', '49': '3B', '4A': 'D6', '4B': 'B3', '4C': '29', '4D': 'E3', '4E': '2F', '4F': '84', '50': '53',
         '51': 'D1', '52': '00', '53': 'ED', '54': '20', '55': 'FC', '56': 'B1', '57': '5B', '58': '6A', '59': 'CB',
         '5A': 'BE', '5B': '39', '5C': '4A', '5D': '4C', '5E': '58', '5F': 'CF', '60': 'D0', '61': 'EF', '62': 'AA',
         '63': 'FB', '64': '43', '65': '4D', '66': '33', '67': '85', '68': '45', '69': 'F9', '6A': '02', '6B': '7F',
         '6C': '50', '6D': '3C', '6E': '9F', '6F': 'A8', '70': '51', '71': 'A3', '72': '40', '73': '8F', '74': '92',
         '75': '9D', '76': '38', '77': 'F5', '78': 'BC', '79': 'B6', '7A': 'DA', '7B': '21', '7C': '10', '7D': 'FF',
         '7E': 'F3', '7F': 'D2', '80': 'CD', '81': '0C', '82': '13', '83': 'EC', '84': '5F', '85': '97', '86': '44',
         '87': '17', '88': 'C4', '89': 'A7', '8A': '7E', '8B': '3D', '8C': '64', '8D': '5D', '8E': '19', '8F': '73',
         '90': '60', '91': '81', '92': '4F', '93': 'DC', '94': '22', '95': '2A', '96': '90', '97': '88', '98': '46',
         '99': 'EE', '9A': 'B8', '9B': '14', '9C': 'DE', '9D': '5E', '9E': '0B', '9F': 'DB', 'A0': 'E0', 'A1': '32',
         'A2': '3A', 'A3': '0A', 'A4': '49', 'A5': '06', 'A6': '24', 'A7': '5C', 'A8': 'C2', 'A9': 'D3', 'AA': 'AC',
         'AB': '62', 'AC': '91', 'AD': '95', 'AE': 'E4', 'AF': '79', 'B0': 'E7', 'B1': 'C8', 'B2': '37', 'B3': '6D',
         'B4': '8D', 'B5': 'D5', 'B6': '4E', 'B7': 'A9', 'B8': '6C', 'B9': '56', 'BA': 'F4', 'BB': 'EA', 'BC': '65',
         'BD': '7A', 'BE': 'AE', 'BF': '08', 'C0': 'BA', 'C1': '78', 'C2': '25', 'C3': '2E', 'C4': '1C', 'C5': 'A6',
         'C6': 'B4', 'C7': 'C6', 'C8': 'E8', 'C9': 'DD', 'CA': '74', 'CB': '1F', 'CC': '4B', 'CD': 'BD', 'CE': '8B',
         'CF': '8A', 'D0': '70', 'D1': '3E', 'D2': 'B5', 'D3': '66', 'D4': '48', 'D5': '03', 'D6': 'F6', 'D7': '0E',
         'D8': '61', 'D9': '35', 'DA': '57', 'DB': 'B9', 'DC': '86', 'DD': 'C1', 'DE': '1D', 'DF': '9E', 'E0': 'E1',
         'E1': 'F8', 'E2': '98', 'E3': '11', 'E4': '69', 'E5': 'D9', 'E6': '8E', 'E7': '94', 'E8': '9B', 'E9': '1E',
         'EA': '87', 'EB': 'E9', 'EC': 'CE', 'ED': '55', 'EE': '28', 'EF': 'DF', 'F0': '8C', 'F1': 'A1', 'F2': '89',
         'F3': '0D', 'F4': 'BF', 'F5': 'E6', 'F6': '42', 'F7': '68', 'F8': '41', 'F9': '99', 'FA': '2D', 'FB': '0F',
         'FC': 'B0', 'FD': '54', 'FE': 'BB', 'FF': '16'}

for key in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0A', '0B', '0C', '0D', '0E', '0F']:
    if key not in s_box:
        print(f"Key {key} not found in s_box")



def key_expansion(key):
    # Round constants
    round_constants = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

    # Initialize empty key schedule
    key_schedule = [[0 for _ in range(4)] for _ in range(44)]

    # Fill the initial words of the key schedule with the input key
    key_len = len(key)
    for i in range(key_len // 4):
        for j in range(4):
            key_schedule[i][j] = ord(key[i * 4 + j])

    # Fill the remaining words of the key schedule with zeros
    for i in range(key_len // 4, 4):
        for j in range(4):
            key_schedule[i][j] = 0

    # Expand the key schedule
    for i in range(4, 44):
        if i % 4 == 0:
            # Perform g function
            temp = key_schedule[i - 4].copy()
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= round_constants[(i // 4) - 1]
            for j in range(4):
                key_schedule[i][j] = key_schedule[i - 4][j] ^ temp[j]
        else:
            for j in range(4):
                key_schedule[i][j] = key_schedule[i - 4][j] ^ key_schedule[i - 1][j]

    return key_schedule

def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]
    return [sbox[byte] for byte in word]

# add round operation
def inv_add_round_key(state, round_key):
    """
    Performs the AES Inverse Add Round Key operation.
    
    Args:
        state (list): A 4x4 matrix representing the state
        round_key (list): A 4x4 matrix representing the round key
    
    Returns:
        list: A 4x4 matrix representing the result of XORing the state and round key
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            result[i][j] = state[i][j] ^ round_key[i][j]
    
    for i in range (0,4):
        for j in range (0,4):
            hold = hex(result[i][j])
            result[i][j] = hold
    return result

# sub byte operation
def sub_byte(state):
    """
    Performs the AES SubBytes operation on the given state matrix.
    
    Args:
        state (list): A 4x4 matrix representing the state
    
    Returns:
        list: A 4x4 matrix representing the result of the SubBytes operation
    """
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(len(state)):
        for j in range(len(state)):
            hold = (state[i][j])[2:]  # Extract hexadecimal string from the state matrix
            # Ensure hexadecimal string is two characters long
            hold = hold.zfill(2)
            # Convert hexadecimal string to uppercase
            hold = hold.upper()
            result[i][j] = s_box[hold]  # Substitute byte using the S-box lookup table
    
    return result




 # shift row
def inv_shift_rows(state):
    """
    Performs the AES Inverse Shift Rows operation on the given state matrix.
    
    Args:
        state (list): A 4x4 matrix representing the state
    
    Returns:
        list: A 4x4 matrix representing the result of the Inverse Shift Rows operation
    """
    result = [row[:] for row in state]  # Create a copy of the state matrix
    
    # Shift rows
    for i in range(1, 4):
        shift = i
        result[i] = result[i][-shift:] + result[i][:-shift]
    
    # Convert hexadecimal strings to integers
    for i in range(4):
        for j in range(4):
            result[i][j] = int(result[i][j], 16)
    
    return result


# mix coloumn
def multiply_polynomials(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        if a & 0x80:
            a = (a << 1) ^ 0x1b
        else:
            a <<= 1
        b >>= 1
    return p & 0xff

def inv_mix_col(state):
    for i in range(4):
        a = [state[j][i] for j in range(4)]
        b = [0, 0, 0, 0]
        for j in range(4):
            for k in range(4):
                b[j] ^= multiply_polynomials(inv_mix_col_matrix[j][k], a[k])
        for j in range(4):
            state[j][i] = b[j]
    return state


def aes_encrypt(plaintext, initial_key):
    # Key Expansion
    key_schedule = key_expansion(initial_key)

    # Convert plaintext to a 4x4 matrix (state)
    state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[j][i] = ord(plaintext[i * 4 + j])  # Fill the state with plaintext bytes

    # Initial Round Key Addition
    state = inv_add_round_key(state, key_schedule[:4])

    # Rounds
    for round in range(1, 10):
        state = sub_byte(state)
        state = inv_shift_rows(state)
        state = inv_mix_col(state)
        round_key = key_schedule[4 * round : 4 * (round + 1)]
        state = inv_add_round_key(state, round_key)

    # Final Round (without MixColumns)
    state = sub_byte(state)
    state = inv_shift_rows(state)
    round_key = key_schedule[40:]
    state = inv_add_round_key(state, round_key)

    # Convert state to ciphertext
    ciphertext = ""
    print(state)
    for i in range(4):
        for j in range(4):
            ciphertext += chr(int(state[j][i], 16))  # Convert hexadecimal string to character

    return ciphertext

# Example usage
plaintext = "i'm supriyo how are"
initial_key = "0123456789abcdef"
ciphertext = aes_encrypt(plaintext, initial_key)
print("Ciphertext:", ciphertext)
