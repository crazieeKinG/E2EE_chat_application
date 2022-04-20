def string_to_ascii(input):
    return [ord(a) for a in input]

def ascii_to_string(input):
    characters = [chr(a) for a in input]
    actual_string = ""
    for character in characters:
        actual_string += character 
    return actual_string

def convert_16_bit(input):
    input_16_bit = (input[0] * 256) + input[1]    
    return input_16_bit