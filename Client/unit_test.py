from IDEA.Operations.addition_modulo import addition_inverse, additive_modulo
from IDEA.Operations.ascii_operation import ascii_to_string, string_to_ascii, convert_16_bit
from IDEA.Operations.multiplication_modulo import multiplication_modulo, multiplication_inverse
from IDEA.Operations.bitwise_xor import bitwise_XOR
from IDEA.key_generation import shift_left, break_key, key_decimal_value

def test_ascii_to_string():
    assert ascii_to_string([72, 101, 108, 108, 111]) == "Hello"

def test_string_to_ascii():
    assert string_to_ascii("Hello") == [72, 101, 108, 108, 111]

def test_convert_16_bit():
    assert convert_16_bit([28, 87]) == 7255

def test_bitwise_xor():
    assert bitwise_XOR([14], [20]) == [26]

def test_multiplication_modulo():
    assert multiplication_modulo([20, 29], [98, 92]) == [76, 178]

def test_multiplication_inverse():
    assert multiplication_inverse([67, 92]) == [57, 120]

def test_addition_modulo():
    assert additive_modulo([33, 45], [14, 4]) == [47, 49]

def test_addition_inverse():
    assert addition_inverse([4, 2]) == [251, 254]

def test_shift_key():
    assert shift_left(7729) == 259342204928

def test_break_key():
    assert break_key(7729) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 49]

def test_key_decimal_value():
    assert key_decimal_value([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 49]) == 7729
