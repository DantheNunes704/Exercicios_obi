posicoes = int(input())
pingos = int(input())
fita = {}

quant_dias = 0
contador = 0
for n in range(0, posicoes-1):
    fita[contador] = 0
    contador += 1

controle = 0
for n in range(0, len(fita)-1):
    controle += 1
    posicao = int(input())
    fita[posicao-1] = 1
    if controle == pingos:
        break
    
registro = 0 # verifica quantos índices na fita estão com tinta

for n in range(len(fita)-1):
    if n == 1:
        registro += 1

if registro < len(fita):
    
    while registro < len(fita)-1:
        contador = 0
        registro = 0
        for n in fita:
            if n == 1 and contador > 0 and contador+1 < len(fita):
                fita[contador-1] = 1
                fita[contador+1] = 1
                contador += 1
            elif n == 1 and contador+1 < len(fita):
                fita[contador+1] = 1
                contador += 1
            elif n == 1 and contador-1 >= 0:
                fita[contador-1] = 1
                contador += 1
            
            contador += 1
            
        quant_dias += 1
            
        for n in range(0, len(fita)-1):
            if n == 1:
                registro += 1

print(quant_dias)