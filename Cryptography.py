import math
import random


chave = input("Escreva uma mensagem: ")
chaveCifrada = []
chaveCifradaTemp = []
chaveDecifrada = []
chaveDecifradaTemp = []
n,d,e,m = None,None,None,None

def sort_prime(num):
    num1_primo = []
    num2_primo = [True] * (num + 1)
    for i in range(2, num + 1):
        if num2_primo[i]:
            num1_primo.append(i)
            for j in range(2, int(num / i) + 1):
                num2_primo[i * j] = False
    return num1_primo

def get_random_int(min, max):
    min = math.ceil(min)
    max = math.floor(max)
    return math.floor(random.random() * (max - min + 1)) + min

def mdc(x,y):
    while(y) :
        t=y
        y=x%y
        x=t
    return x

def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

# Aumentar muito esse valor vai deixar a conta muito mas MUITO LENTA
primos = sort_prime(300)

p = primos[get_random_int(len(primos)-60,len(primos))]
q = primos[get_random_int(len(primos)-60,len(primos))]

n = p*q
m = (p-1)*(q-1)

tempE = 0
temp=(get_random_int(1,m))
e=0
while(e==0) :
    tempE = mdc(temp,m)
    if tempE==1 : e = temp
    else : temp=(get_random_int(1,m))

d = modInverse(e,m)

print("p:",p)
print("q:",q)
print("n:",n)
print("m:",m)
print("e:",e)
print("d:",d)


strBytes = bytes(chave, 'utf-8')
# bytes atuais na string
for byte in strBytes:
    chaveCifradaTemp.append(byte)

print('mensagem convertida para bytes: ')
print(chaveCifradaTemp)

for index in range(len(chaveCifradaTemp)):
    temp = pow(chaveCifradaTemp[index],e)
    temp2 = temp % n
    chaveCifrada.append(temp2)

print('\n')
print('mensagem criptografada: ')
print(chaveCifrada)



for index in range(len(chaveCifrada)):
    temp = pow(chaveCifrada[index],e)
    temp2 = temp % n
    chaveDecifradaTemp.append(pow(chaveCifrada[index],d) % n)

revelar = input("Mostrar mensagem traduzida?(sim, yes, si, não, no): ")

if revelar == "sim" or "yes" or "si":
    print('\n')
    print('mensagem decriptografada: ')
    print(chaveDecifradaTemp)

    msgDecifrada = bytes(chaveDecifradaTemp)

    print('\n')
    print('mensagem traduzida: ')
    print(msgDecifrada)
else:
    print("remo")
