import random
import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('params', nargs='*', help='figure, number, character')
args = parser.parse_args()

def make_password(figure, number, chars):
    for i in range(number):
        yield ''.join([random.choice(chars) for i in range(figure)])

def get_default_params():
    figure = 8
    number = 10
    character = default=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return [figure, number, character]

def set_params():
    params = get_default_params()
    if 0 < len(args.params): params[0] = int(args.params[0])
    if 1 < len(args.params): params[1] = int(args.params[1])
    if 2 < len(args.params): params[2] = args.params[2]
    return params

def PRINT_password(figure, number, character):
    for pw in make_password(figure, number, character):
        print pw

params = set_params()
print params[0], params[1], params[2] 
PRINT_password(*params);
