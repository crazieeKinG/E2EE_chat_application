from .ascii_operation import convert_16_bit

BLOCKSIZE = 2**16 + 1

def multiplication_modulo(input_1, input_2):
    # print("in1:"+str(input_1))
    # print("in2:"+str(input_2))

    input_16_bit_1 = convert_16_bit(input_1)
    input_16_bit_2 = convert_16_bit(input_2)
    # print("in-1:"+str(input_16_bit_1))
    # print("in-2:"+str(input_16_bit_2))

    mul = input_16_bit_1 * input_16_bit_2
    output = mul % BLOCKSIZE
    # print("out:"+str(output))

    output_8bit_2 = output % 256
    output_8bit_1 = (output - output_8bit_2) / 256
    # print("out_1:"+str(output_8bit_1))
    # print("out_2:"+str(output_8bit_2))

    return [int(output_8bit_1), output_8bit_2]

def multiplication_inverse(key):
    key_16_bit = convert_16_bit(key)
    for j in range(BLOCKSIZE-1):
        x = (key_16_bit * j) % BLOCKSIZE
        if x == 1:
            inverse_key = j
            break

    output_8bit_2 = inverse_key % 256
    output_8bit_1 = (inverse_key - output_8bit_2) / 256
    # print("out_1:"+str(output_8bit_1))
    # print("out_2:"+str(output_8bit_2))
    return [int(output_8bit_1), output_8bit_2]