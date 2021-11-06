import array
'''
    Cryptography & Information Security
    Abdul Hannan Ayubi
    20210290
'''
def Calculate(firstNumber, secondNumber, generatorNumber, primeNumber):
    resultOne = pow(generatorNumber, firstNumber) % primeNumber
    resultTwo = pow(generatorNumber, secondNumber) % primeNumber
    print(resultOne,resultTwo)
    finalResultOne = pow(resultOne, secondNumber) % primeNumber
    finalResultTwo = pow(resultTwo, firstNumber) % primeNumber

    return finalResultOne, finalResultTwo

def GettingInputs():
    primeNumber = int(input("Enter prime number :"))
    generatorNumber = int(input("Enter generator :"))
    firstNumber = int(input("Enter first number :"))
    secondNumber = int(input("Enter second number :"))
    return primeNumber,generatorNumber,firstNumber,secondNumber


primeNumber, generatorNumber, firstNumber, secondNumber = GettingInputs()

finalResultOne , finalResultTwo = Calculate(firstNumber,secondNumber,generatorNumber,primeNumber)

if finalResultOne == finalResultTwo:
    print(f"The Value K = {finalResultOne} is the same for both")