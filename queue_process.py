from collections import deque

palavras = input("")

fila = deque()

for palavra in palavras.split():
    fila.append(palavra)
    
print(fila)

while fila:
    palavra = fila.popleft()
    if 'o' in palavra:
        print(palavra)