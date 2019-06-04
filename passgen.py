import passgen.passgen
import argparse

parser = argparse.ArgumentParser(description='Password and Passphrase Generator', allow_abbrev=False)
parser.add_argument('-passwordgen', '--p', help='generate a password', action='store_true')
parser.add_argument('-passphrasegen', '--pr', help='generate a passphrase', action='store_true')
parser.add_argument('-mixedgen', '--mg', help='generate passphrase with symbols and digits', action='store_true' )
args = parser.parse_args()

if (args.mg is True):

    mixed_obj = passgen.passgen.mixedgen()
    final_mixgen_passphrase = mixed_obj.create_mixedgen()
    print(f'The generated mixed passphrase is : {final_mixgen_passphrase}')

elif(args.p is True):
    print("Enter the number of characters that you want in your password :")
    input_characters = int(input())
    if input_characters < 0:
        input_characters = 8
    elif 0 < input_characters < 8:
        input_characters = 8
    else:
        print(f'Creating password that consists of {input_characters} characters.')

    pwd_obj = passgen.passgen.password_gen(input_characters)
    final_password = pwd_obj.create_password(input_characters)
    uncommon_password = pwd_obj.check_password(final_password)

    print(f'The generated password is : {uncommon_password}.')

elif(args.pr is True):
    print('Enter the number of words to be included in your passphrase')
    count = int(input())
    passphrase = ''
    passphrase_obj = passgen.passgen.passphrase_gen()
    while(count > 0):
        passphrase = (passphrase) + (passphrase_obj.create_passphrase())
        count = count - 1
    print(f'The generated passphrase is : {passphrase}')
else:
    print('Something went wrong.')
