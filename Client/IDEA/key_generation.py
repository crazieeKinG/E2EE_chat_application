from math import floor
import random

#Userdefinded modules
from IDEA.Operations.multiplication_modulo import multiplication_inverse
from IDEA.Operations.addition_modulo import addition_inverse

def first_key():
    key = list()
    for i in range(16):
        character = random.randint(0,255)
        key.append(character)
    return key

def shift_left(n):
    bits = 25
    total_bit = 128
    return ((n << bits) % (1 << total_bit)) | (n >> (total_bit - bits))

def break_key(key):
    key_list = list()
    prev_key = 0
    for i in range(16):
        prev_key = (key - prev_key) % (256**(i+1))
        character = floor(prev_key / (256**(i)))
        key_list.append(character)
    key_list.reverse()
    return key_list
    
def key_decimal_value(key):
    value = 0
    for i in range(16):
        value += (key[i] * (256**(15-i)))
    return value

def create_key():
    key = list()
    key_value = 0
    for i in range(9):
        if i == 0:
            new_round_key = first_key()
            key_value = key_decimal_value(new_round_key)
        else:
            shift_key = shift_left(key_value)
            new_round_key = break_key(shift_key)
            key_value = key_decimal_value(new_round_key)
        key.append(new_round_key)
    encryption_key = key.copy()
    decryption_key = list()
    key.reverse()
    for i in range(9):
        k1 = multiplication_inverse([key[i][0], key[i][1]])
        k2 = addition_inverse([key[i][2], key[i][3]])
        k3 = addition_inverse([key[i][4], key[i][5]])
        k4 = multiplication_inverse([key[i][6], key[i][7]])
        next_index = (i + 1) % 9
        decryption_key.append(k1+k2+k3+k4+[key[next_index][8], key[next_index][9], key[next_index][10], key[next_index][11], key[next_index][12], key[next_index][13], key[next_index][14], key[next_index][15]])
    return {'encryption_key': encryption_key, 'decryption_key': decryption_key}