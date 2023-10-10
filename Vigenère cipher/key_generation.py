import random

char_list = ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
def generation():
    with open("Vigenère cipher/key/key.txt", 'w') as key:
        key.write('')
    with open("Vigenère cipher/key/key.txt", 'a') as key:
        for i in range(256):
            key.write(random.choice(char_list))

    
