import random
import string

figure = 8
number = 10
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
for i in range(number):
    print(''.join([random.choice(chars) for i in range(figure)]))