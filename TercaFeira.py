from collections import deque

def Invert(frase):
    stack = deque()
    
    for palavra in frase.split():
        stack.append(palavra)
        
    frase_invertida = []
    
    while stack:
        frase_invertida.append(stack.pop()) 
    
    return ' '.join(frase_invertida)

frase = "Esta é uma frase de exemplo"
frase_invertida = Invert(frase)
print(frase_invertida)  # Saída: "exemplo de frase uma é Esta"