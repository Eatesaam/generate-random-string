import random
import string


def getString():
    # generate 3 uppercase letter 
    x = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    # generate 3 digits
    y = ''.join(random.choice(string.digits) for _ in range(3))
    # generate 1 uppercase letter
    z = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))

    st = x+y+z

    return st

def main():
    st = getString()
    print(st)


if __name__=='__main__':
    main()
