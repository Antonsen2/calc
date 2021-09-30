def plus(a, b):
    return a + b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def sub(a, b):
    return a - b


def rem(a, b):
    return a % b


def square(a, b):
    return a ** b


def square_root(a, b=2):
    b = 1/b
    return a ** b
  

def floor(a):
    return int(a)


def ceil(a):
    return int(a) + 1


def main():

    print(plus(4, 7))
    print(mult(10, 11))
    print(sub(50, 34))
    print(div(4000, 100))
    print(square(3, 2))
    print(square_root(49))


if __name__ == '__main__':
    main()
