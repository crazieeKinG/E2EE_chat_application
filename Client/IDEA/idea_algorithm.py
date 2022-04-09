from .Operations.ascii_operation import ascii_to_string, string_to_ascii
from .Operations.addition_modulo import additive_modulo
from .Operations.multiplication_modulo import multiplication_modulo
from .Operations.bitwise_xor import bitwise_XOR


def operate(input, key):
    result_text = list()

    message_length = len(input)
    if message_length % 8 != 0:
        input += " "*(8-(message_length%8))
        
    input_ascii = string_to_ascii(input)

    iterations = int(len(input_ascii) / 8)

    for j in range(0,iterations):
        p1 = [input_ascii[(j*8)+0], input_ascii[(j*8)+1]]
        p2 = [input_ascii[(j*8)+2], input_ascii[(j*8)+3]]
        p3 = [input_ascii[(j*8)+4], input_ascii[(j*8)+5]]
        p4 = [input_ascii[(j*8)+6], input_ascii[(j*8)+7]]

        for i in range(8):
            k1 = [key[i][0], key[i][1]]
            k2 = [key[i][2], key[i][3]]
            k3 = [key[i][4], key[i][5]]
            k4 = [key[i][6], key[i][7]]
            k5 = [key[i][8], key[i][9]]
            k6 = [key[i][10], key[i][11]]

            d1 = multiplication_modulo(p1, k1)
            d2 = additive_modulo(p2, k2)
            d3 = additive_modulo(p3, k3)
            d4 = multiplication_modulo(p4, k4)
            d5 = bitwise_XOR(d1, d3)
            d6 = bitwise_XOR(d2, d4)
            d7 = multiplication_modulo(d5, k5)
            d8 = additive_modulo(d6, d7)
            d9 = multiplication_modulo(d8, k6)
            d10 = additive_modulo(d7, d9)
            d11 = bitwise_XOR(d1, d9)
            d12 = bitwise_XOR(d3, d9)
            d13 = bitwise_XOR(d2, d10)
            d14 = bitwise_XOR(d4, d10)

            p1 = d11
            p2 = d13
            p3 = d12
            p4 = d14
        
        k1 = [key[8][0], key[8][1]]
        k2 = [key[8][2], key[8][3]]
        k3 = [key[8][4], key[8][5]]
        k4 = [key[8][6], key[8][7]]

        d1 = multiplication_modulo(p1, k1)
        d2 = additive_modulo(p2, k2)
        d3 = additive_modulo(p3, k3)
        d4 = multiplication_modulo(p4, k4)

        result_text.extend(d1+d2+d3+d4)
            
    return ascii_to_string(result_text)
