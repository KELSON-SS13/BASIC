'''
# FUNCAO SOMA 3 PARAMETROS

def soma (a,b,c):
    return a+b+c
a=int(input('Digite o 1 numero: '))
b=int(input('Digite o 2 numero: '))
c=int(input('Digite o 3 numero: '))
print(soma(a,b,c))

 '''
'''
# FUNCAO RECEBE NUMERO E PORCENTAGEM A SER ACRESCENTADO
def porcen (a,b):
    return a + (a*(b/100))
print(porcen(200,20))
'''

def fizzbuzz (a):
    if a % 15 == 0:
        return "FIZZBUZZ"
    elif a % 3 == 0:
        return  "BUZZ"
    elif a % 5 == 0:
        return "FIZZ"
    else:
        return a
a=-1
while a != 0:
    a=int(input('Digite o 1 numero: '))
    print(fizzbuzz(a))