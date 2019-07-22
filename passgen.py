import passgen.passgen
import argparse

parser = argparse.ArgumentParser(description='Password and Passphrase Generator', allow_abbrev=False)
parser.add_argument('-passwordgen', '--p', help='generate a password', action='store_true')
parser.add_argument('-passphrasegen', '--pr', help='generate a passphrase', action='store_true')
parser.add_argument('-mixedgen', '--mg', help='generate passphrase with symbols and digits', action='store_true' )
args = parser.parse_args()

if (args.mg is True):

    h = passgen.passgen.mixedgen
    final_mixgen_passphrase = h.create_mixedgen()
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

    p = passgen.passgen.password_gen()
    final_password = p.create_password(input_characters)
    uncommon_password = p.check_password(final_password, input_characters)

    print(f'The generated password is : {uncommon_password}.')

elif(args.pr is True):
    print('Enter the number of words to be included in your passphrase')
    count = int(input())
    passphrase = ''
    while(count > 0):
        phr = passgen.passgen.passphrase_gen()
        passphrase = (passphrase) + (phr.create_passphrase())
        count = count - 1
    print(f'The generated passphrase is : {passphrase}')
else:
    print('Something went wrong.')
