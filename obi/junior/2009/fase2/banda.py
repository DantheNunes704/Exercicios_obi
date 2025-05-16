n1, n2 = map(int, input().split())

musicos_numeros = [];
musicos = [];

for n in range(n1):
    musicos.append(0);
    
for n in range(n1):
    musicos_numeros.append(n+1);
    
for n in range(n2):
    lista_aux = input().split();
    
    musicos[int(lista_aux[0])-1] += int(lista_aux[2]);

for n in range(n1):
    for d in range(n1-1):
        if musicos[d] < musicos[d+1]:
            aux = musicos[d];
            musicos[d] = musicos[d+1];
            musicos[d+1] = aux;
            
            aux2 = musicos_numeros[d];
            musicos_numeros[d] = musicos_numeros[d+1];
            musicos_numeros[d+1] = aux2;
        
    
print(musicos_numeros[0], musicos_numeros[1], musicos_numeros[2]);