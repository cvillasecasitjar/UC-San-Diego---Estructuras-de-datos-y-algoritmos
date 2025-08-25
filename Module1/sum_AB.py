def sumar(a, b):
    return a + b


if __name__ == "__main__":
    print("Please enter two numbers:")
    a, b = map(int, input().split())
    print("You entered:", a, b)
    print(sumar(a, b))