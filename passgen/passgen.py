import string
import secrets
import os


special_char = '!"#$%&\'()*+,-./:;?@[]^_`{|}~'
password_file = os.path.abspath('10k-common-passwords.txt')
passphrase_file = os.path.abspath('passphrase-wordlist-copy.txt')
passphrase_word_count = 4


class password_gen:

    def pick_number(self):
        secure_number = string.digits[secrets.randbelow(10)]
        return secure_number

    def pick_lowercase(self):
        secure_lowercase_alphabet = string.ascii_lowercase[secrets.randbelow(26)]

        return secure_lowercase_alphabet

    def pick_uppercase(self):
        secure_uppercase_alphabet = string.ascii_uppercase[secrets.randbelow(26)]
        return secure_uppercase_alphabet

    def pick_special_char(self):
        secure_special_char = special_char[secrets.randbelow(30)]
        return secure_special_char

    secret_function_list = [pick_lowercase, pick_number, pick_special_char, pick_uppercase]

    def create_password(input_characters):
        password = ''
        for i in range(input_characters):
            temp = (password_gen.secret_function_list[secrets.randbelow(4)])()
            password += temp
        return password

    def check_password(final_password, input_characters):
        cp_file = open(password_file, 'r')

        for line in cp_file:
            if final_password == line[0:-1]:
                final_password = password_gen.create_password(input_characters)
                print('Match found. Re-generating.')
            else:
                continue
        return final_password


class passphrase_gen:

    def create_passphrase(self):
        bit_0 = bit_1 = bit_2 = bit_3 = 0
        while ((bit_0 < 1) or (bit_0 > 6)):
            bit_0 = secrets.randbelow(10)
        bit_0 = str(bit_0)
        while ((bit_1 < 1) or (bit_1 > 6)):
            bit_1 = secrets.randbelow(10)
        bit_1 = str(bit_1)
        while ((bit_2 < 1) or (bit_2 > 6)):
            bit_2 = secrets.randbelow(10)
        bit_2 = str(bit_2)
        while ((bit_3 < 1) or (bit_3 > 6)):
            bit_3 = secrets.randbelow(10)
        bit_3 = str(bit_3)

        dice_num = bit_0+bit_1+bit_2+bit_3

        with open(passphrase_file, "r") as wordlist_file:
            for item in wordlist_file:
                if(item[0:4] == dice_num):
                    return item[5:-1]


class mixedgen:

    def create_mixedgen(self):
        print('Enter the number of words that you would like to include in the mixed passphrase.')
        mix_count = int(input())
        mixedgen_list = [password_gen.pick_lowercase, password_gen.pick_uppercase, password_gen.pick_number, password_gen.pick_special_char]
        mixed_passphrase = ''

        while(mix_count > 0):
            if(secrets.randbelow(3) > 1):
                mixed_passphrase = mixed_passphrase + mixedgen_list[secrets.randbelow(4)]()
                mix_count = mix_count - 1
            else:
                mixed_passphrase = mixed_passphrase + passphrase_gen.create_passphrase()
                mix_count = mix_count - 1

        return (mixed_passphrase)
