from .ascii_operation import convert_16_bit

BLOCKSIZE = 2**16

def additive_modulo(input_1, input_2):
    # print("in1:"+str(input_1))
    # print("in2:"+str(input_2))

    input_16_bit_1 = convert_16_bit(input_1)
    input_16_bit_2 = convert_16_bit(input_2)
    # print("in-1:"+str(input_16_bit_1))
    # print("in-2:"+str(input_16_bit_2))

    sum = input_16_bit_1 + input_16_bit_2
    output = sum % BLOCKSIZE
    # print("out:"+str(output))

    output_8bit_2 = output % 256
    output_8bit_1 = (output - output_8bit_2) / 256
    # print("out_1:"+str(output_8bit_1))
    # print("out_2:"+str(output_8bit_2))

    return [int(output_8bit_1), output_8bit_2]

def addition_inverse(key):
    input_16_bit = convert_16_bit(key)
    # print("in k"+str(input_16_bit))
    inverse_key = (BLOCKSIZE - input_16_bit) % BLOCKSIZE
    # print("inv k"+str(inverse_key))
    output_8bit_2 = inverse_key % 256
    output_8bit_1 = (inverse_key - output_8bit_2) / 256
    # print("out_1:"+str(output_8bit_1))
    # print("out_2:"+str(output_8bit_2))

    return [int(output_8bit_1), output_8bit_2]
