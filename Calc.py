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

    print("this is the calculator try out its functions!")
    print("This is the functions plus, mult, sub, div, square")
    user_choice = input("Enter a function: ")
    running = True
    while running:
        if user_choice == "plus":
            x = int(input("enter the first number: "))
            y = int(input("enter the second: "))
            print(plus(x, y))

        if user_choice == "sub":
            x = int(input("enter the first number: "))
            y = int(input("enter the second: "))
            print(sub(x, y))

        if user_choice == "mult":
            x = int(input("enter the first number: "))
            y = int(input("enter the second: "))
            print(mult(x, y))


if __name__ == '__main__':
    main()
