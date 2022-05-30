
def add():
    a=int(input("Enter"))
    b=int(input("Enter"))
    return a,b


def output(a, b):
    sum=a+b
    print("sun of a and b is:",sum)


def main():
    a,b=add()
    output(a, b)


if __name__ == '__main__':
    main()
