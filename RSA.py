import array

'''
    Cryptography & Information Security
    Abdul Hannan Ayubi
    20210290
'''

import array


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def findTheDNumber(_e, _d, _ph):
    while True:
        if ((_e * _d) % _ph) == 1 and ((_e * _d) % _ph) == 1:
            break
        _d = _d + 1

    for i in range(0, _ph):
       print(f"d : {((i * _ph) + 1) / _e}")

    return _d


def getInput():
    p_Name = int(input("Enter p :"))
    q_Name = int(input("Enter q : "))
    e_Name = int(input("Enter e : "))

    return p_Name, q_Name, e_Name


def _Encrypt(_arr):
    temp = []
    for m in _arr:
        temp.append(pow(m, e) % n)
    return temp


def _Decrypt(_arr):
    temp = []
    for k in _arr:
        temp.append(pow(k, result) % n)
    print(temp)


p, q, e = getInput()
n = p * q

ph = (p - 1) * (q - 1)


def EncsignSignature(temp, n, privateKey):
    arrtemp = []
    for i in temp:
        arrtemp.append(pow(i, privateKey) % n)

    return arrtemp


def getEValue(_e):
    value = 1
    for i in range(0, _e + 1):
        if gcd(i, ph) == 1 and i < ph:
            value = i
            print(f"E : {i}")
    return value


e = getEValue(e)

result = findTheDNumber(e, 1, ph)

print("d : ", result)
print(f"Public key ({e}, {n})")
print(f"Private key ({result}, {n})")

str_input = input("Enter plane text : ")
arr = []
for letter in str_input:
    number = (ord(letter) - 96)
    arr.append(number)

print("The numeric values of alphabet")
print(arr)

print("Encrypted Data")
print(_Encrypt(arr))

print("Decrypted Data")
_Decrypt(_Encrypt(arr))
