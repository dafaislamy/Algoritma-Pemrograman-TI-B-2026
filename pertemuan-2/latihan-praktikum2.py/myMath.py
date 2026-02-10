def penambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        print('Pembagian tidak dapat dilakukan karena pembagi bernilai 0')
    else:
        return a / b
    
def modulus(a, b):
    return a % b

def fibonacci(n):
    deret = []
    a, b = 0, 1
    for i in range(n):
        deret.append(a)
        a, b = b, a + b
    return deret