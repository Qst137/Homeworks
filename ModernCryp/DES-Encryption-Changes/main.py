"""
@FileName: main
@Description: 现代密码学作业 2
@Author: qst137
@Version: demo
"""
from copy import *

ip_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

ip_table_re = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_boxes = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],

    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P_table = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


# IP置换
def ip_displace(input_bits):
    assert len(input_bits) == 64
    displaced_bits = [input_bits[i - 1] for i in ip_table]
    return displaced_bits


# IP逆置换
def ip_displace_re(input_bits):
    assert len(input_bits) == 64
    displaced_bits = [input_bits[i - 1] for i in ip_table_re]
    return displaced_bits


# E扩展
def e_expand(input_bits):
    assert len(input_bits) == 32
    expanded_bits = [input_bits[i - 1] for i in E_table]
    return expanded_bits


# S盒置换
def s_boxes_displace(input_bits):
    assert len(input_bits) == 48
    output_bits = []
    for i in range(8):
        s_box = S_boxes[i]
        bits_6 = deepcopy(input_bits[6 * i:6 * i + 6])
        s_row = bits_6[0] * 2 + bits_6[5]
        s_column = bits_6[1] * 8 + bits_6[2] * 4 + bits_6[3] * 2 + bits_6[4]
        bits_4_num = s_box[s_row][s_column]
        bits_4 = [(bits_4_num >> 3) & 1, (bits_4_num >> 2) & 1, (bits_4_num >> 1) & 1, bits_4_num & 1]
        output_bits += bits_4
    return output_bits


# P置换
def p_displace(input_bits):
    assert len(input_bits) == 32
    displaced_bits = [input_bits[i - 1] for i in P_table]
    return displaced_bits


# 轮函数
def round_func(r_bits, k_bits):
    assert len(r_bits) == 32 and len(k_bits) == 48
    expanded_bits = e_expand(r_bits)
    xor_bits = [(expanded_bits[i] ^ k_bits[i]) for i in range(48)]
    s_bits = s_boxes_displace(xor_bits)
    p_bits = p_displace(s_bits)
    return p_bits


# 生成 key 使用循环移位算法
def keys_generate(key_bits):
    keys = []
    key_bits = [key_bits[bit - 1] for bit in PC1]
    left = key_bits[:28]
    right = key_bits[28:]
    for i in range(16):
        # 循环移位
        left = left[shift_table[i]:] + left[:shift_table[i]]
        right = right[shift_table[i]:] + right[:shift_table[i]]
        combined_key = left + right
        # PC2置换
        sub_key = [combined_key[bit - 1] for bit in PC2]
        keys.append(sub_key)
    return keys


# 对64位消息进行加密
def des_encry_64bits(message, key):
    assert len(message) == 64 and len(key) == 64
    ip_displace(message)
    keys = keys_generate(key)
    left = message[:32]
    right = message[32:]
    for i in range(16):
        buffer = left
        left = right
        rounded = round_func(right, keys[i])
        right = [(buffer[j] ^ rounded[j]) for j in range(32)]
    output_bits = ip_displace_re(left + right)
    return output_bits


key_1 = [
    1, 0, 1, 1, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 1, 1,
    0, 1, 1, 1, 0, 1, 1, 1,
    1, 1, 0, 1, 1, 0, 1, 0,
    0, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 0, 1, 1, 1, 1, 1,
    1, 1, 0, 1, 0, 1, 1, 0
]

message_1 = [
    0, 1, 1, 0, 0, 1, 1, 0,
    1, 0, 1, 1, 0, 0, 1, 1,
    1, 1, 0, 0, 1, 1, 0, 0,
    0, 1, 1, 0, 0, 1, 1, 0,
    1, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 1, 0, 1, 1, 1, 0,
    0, 1, 1, 0, 1, 1, 0, 1,
    0, 1, 1, 0, 1, 1, 1, 1
]


def solve_problem2():
    print("===PROBLEM2===")
    message = "0011100011010101101110000100001011010101001110011001010111100111"
    key = "1010101100110100100001101001010011011001011100111010001011010011"
    message_bits = [int(bit_char) for bit_char in message]
    key_bits = [int(bit_char) for bit_char in key]
    message_bits = ip_displace(message_bits)
    print("IP:" + str(message_bits))
    left_0 = message_bits[:32]
    right_0 = message_bits[32:]
    keys = keys_generate(key_bits)
    left_1 = right_0
    rounded = round_func(right_0, keys[0])
    right_1 = [(left_0[j] ^ rounded[j]) for j in range(32)]
    print("L1:" + str(left_1))
    print("R1:" + str(right_1))


def round_func_without_e(r_bits, k_bits):
    assert len(r_bits) == 32 and len(k_bits) == 48
    r_bits_copy=deepcopy(r_bits)
    for i in range(16):
        r_bits_copy.append(0)
    expanded_bits = r_bits_copy
    xor_bits = [(expanded_bits[i] ^ k_bits[i]) for i in range(48)]
    s_bits = s_boxes_displace(xor_bits)
    p_bits = p_displace(s_bits)
    return p_bits


def s_boxes_displace_fake(input_bits):
    assert len(input_bits) == 48
    output_bits = []
    for i in range(8):
        s_box = S_boxes[i]
        bits_6 = deepcopy(input_bits[6 * i:6 * i + 6])
        bits_4 = bits_6[1:5]
        output_bits += bits_4
    return output_bits


def round_func_without_s(r_bits, k_bits):
    assert len(r_bits) == 32 and len(k_bits) == 48
    expanded_bits = e_expand(r_bits)
    xor_bits = [(expanded_bits[i] ^ k_bits[i]) for i in range(48)]
    s_bits = s_boxes_displace_fake(xor_bits)
    p_bits = p_displace(s_bits)
    return p_bits


def round_func_without_p(r_bits, k_bits):
    assert len(r_bits) == 32 and len(k_bits) == 48
    expanded_bits = e_expand(r_bits)
    xor_bits = [(expanded_bits[i] ^ k_bits[i]) for i in range(48)]
    s_bits = s_boxes_displace_fake(xor_bits)
    return s_bits


def des_encry_64bits_without_e(message_bits, keys):
    message_bits = ip_displace(message_bits)
    print("IP:" + str(message_bits))
    # print(len(message_bits))
    left = deepcopy(message_bits[:32])
    right = deepcopy(message_bits[32:])
    for i in range(6):
        buffer = left
        left = right
        rounded = round_func_without_e(right, keys[i])
        right = [(buffer[j] ^ rounded[j]) for j in range(32)]
        this_bits = left + right
        this_str = ""
        for char in this_bits:
            this_str += str(char)
        print("round {} :".format(i + 1) + this_str)


def des_encry_64bits_without_s(message_bits, keys):
    message_bits = ip_displace(message_bits)
    print("IP:" + str(message_bits))
    left = deepcopy(message_bits[:32])
    right = deepcopy(message_bits[32:])
    print("NO S BOXES")
    for i in range(6):
        buffer = left
        left = right
        rounded = round_func_without_s(right, keys[i])
        right = [(buffer[j] ^ rounded[j]) for j in range(32)]
        this_bits = left + right
        this_str = ""
        for char in this_bits:
            this_str += str(char)
        print("round {} :".format(i + 1) + this_str)


def des_encry_64bits_without_ip(message_bits, keys):
    message_bits = ip_displace(message_bits)
    print("IP:" + str(message_bits))
    left = deepcopy(message_bits[:32])
    right = deepcopy(message_bits[32:])
    print("NO P DISPLACE")
    for i in range(6):
        buffer = left
        left = right
        rounded = round_func_without_p(right, keys[i])
        right = [(buffer[j] ^ rounded[j]) for j in range(32)]
        this_bits = left + right
        this_str = ""
        for char in this_bits:
            this_str += str(char)
        print("round {} :".format(i + 1) + this_str)


def des_encry_64bits_6_rounds(message_bits, keys):
    left = deepcopy(message_bits[:32])
    right = deepcopy(message_bits[32:])
    print("BASIC WAY")
    for i in range(6):
        buffer = left
        left = right
        rounded = round_func(right, keys[i])
        right = [(buffer[j] ^ rounded[j]) for j in range(32)]
        this_bits = left + right
        this_str = ""
        for char in this_bits:
            this_str += str(char)
        print("round {} :".format(i + 1) + this_str)


def solve_problem3():
    print("===PROBLEM3===")
    message = "0011100011010101101110000100001011010101001110011001010111100111"
    message_changed = "1011100011010101101110000100001011010101001110011001010111100111"
    key = "1010101100110100100001101001010011011001011100111010001011010011"
    key_bits = [int(bit_char) for bit_char in key]
    keys = keys_generate(key_bits)
    message_bits = [int(bit_char) for bit_char in message]
    message_bits_changed = [int(bit_char) for bit_char in message_changed]
    print("==BASIC DES==")
    print("EX BITS")
    des_encry_64bits_6_rounds(message_bits, keys)
    print("CHANGED BITS")
    des_encry_64bits_6_rounds(message_bits_changed, keys)
    print("==NO E DISPLACE==")
    print("EX BITS")
    des_encry_64bits_without_e(message_bits, keys)
    print("CHANGED BITS")
    des_encry_64bits_without_e(message_bits_changed, keys)
    print("==NO S BOXES==")
    print("EX BITS")
    des_encry_64bits_without_s(message_bits, keys)
    print("CHANGED BITS")
    des_encry_64bits_without_s(message_bits_changed, keys)
    print("==NO P DISPLACE==")
    print("EX BITS")
    des_encry_64bits_without_ip(message_bits, keys)
    print("CHANGED BITS")
    des_encry_64bits_without_ip(message_bits_changed, keys)


if __name__ == "__main__":
    ciphertext = des_encry_64bits(message_1, key_1)
    print("test message:" + str(message_1))
    print("test ciphertext:" + str(ciphertext))
    solve_problem2()
    solve_problem3()
