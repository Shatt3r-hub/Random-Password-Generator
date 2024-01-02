from sre_constants import CHARSET
from typing import final
from random_password_creator import Password
import argparse

args = argparse.ArgumentParser(description='Random Password Generator !!', epilog='end')
args.add_argument('-l', '--length', default=10, type=int, dest='length', help='length of password')
args.add_argument('-c', '--charset', required=True, help='combinations lowerCase(l/L) upperCase(u/U) digit(d/D) sprcialCharacter(s/S)')
options = args.parse_args()

password = Password(options.charset, options.length)
if(password.set_chararray() == 0):
    args.print_help()
else:
    print("The random password is :",password.pass_generator())

