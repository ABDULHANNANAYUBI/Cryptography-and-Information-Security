import array
'''
    Cryptography & Information Security
    Abdul Hannan Ayubi
    20210290
'''

def GettingInput():
    a = int(input("Enter a:"))
    b = int(input("Enter b: "))
    a1 = int(input("Enter a1: "))
    b1 = int(input("Enter b1: "))
    p = int(input("Enter P: "))

    return a, b, a1, b1, p

a, b, a1, b1, p = GettingInput()

def Calculate(a, b, a1, b1):
    m = (a * b) - 1;
    print(m)
    e = (a1 * m) + a;
    print(e)
    d = (b1 * m) + b;
    print(d)
    n = ((e * d) - 1) / m;
    print(n)
    return e, d, n

e, d, n = Calculate(a, b, a1, b1)

def IfTrue(p, e, d, n):
    enc = (p * e) % n
    print(enc)
    dec = (enc * d) % n
    if dec == p:
        print(f"P-Value: {p} Decrypt : {dec}")
        print(f"Result: {dec}")

IfTrue(p,e,d,n)
