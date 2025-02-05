import random
import string

def gen_pass():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(8))

print(gen_pass())
