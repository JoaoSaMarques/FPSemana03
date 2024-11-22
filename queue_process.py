from collections import deque

palavras = input("")

fila = deque()

for palavra in palavras.split():
    fila.append(palavra)
    
print(fila)