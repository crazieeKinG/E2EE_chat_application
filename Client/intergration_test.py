from IDEA.key_generation import create_key
from IDEA.idea_algorithm import operate

keys = dict()
plainText = ""
cypherText = ""

def test_key_generation():
    global keys
    keys = create_key()
    number_of_encryption_keys = 0
    number_of_decryption_keys = 0
    for x in keys['encryption_key']:
        number_of_encryption_keys += len(x)
    for x in keys['decryption_key']:
        number_of_decryption_keys += len(x)
    assert len(keys['decryption_key']) == 9 
    assert len(keys['encryption_key']) == 9 
    assert number_of_decryption_keys == 144
    assert number_of_encryption_keys == 144

def test_encryption_decryption():
    global keys
    cypherText = operate("Hello! How are you?", keys['encryption_key'])
    plainText = operate(cypherText, keys['decryption_key'])
    assert "Hello! How are you?" == plainText.strip()