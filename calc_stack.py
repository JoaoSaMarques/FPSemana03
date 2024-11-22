from collections import deque

numeros = input("")

pilha = deque()

for numero in numeros.split():
    pilha.append(int(numero))
    
print(pilha)

while pilha:
    numero = pilha.pop()
    print(numero ** 2)