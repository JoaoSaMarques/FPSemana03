from collections import deque

def Invert(frase):
    stack = deque()
    
    for palavra in frase.split():
        stack.append(palavra)
        
    frase_invertida = []