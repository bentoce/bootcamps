# Generator Expressions
from sys import getsizeof


numeros = [x * 10 for x in range(10000)]
print(numeros)
print(type(numeros))
print(getsizeof(numeros))

print('=====================================')

numeros1 = (x * 10 for x in range(1000))
print(numeros1)
print(type(numeros1))
print(getsizeof(numeros1))

