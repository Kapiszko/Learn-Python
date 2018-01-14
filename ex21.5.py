def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract (a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

question = 21 + 33 * 14 / 16
print(question)

question2 = add(21, (divide(multiply(33,14), 16)))
print(question2)
