aux_1 = [];

result_comp = [];
tempo_comp = [];

aux_1 = input().split(" ");

numero = int(aux_1[0]);

for n in range(numero):
    result_comp.append(n+1);
    tempo_comp.append(0);
    lista_aux = [];
    lista_aux = input().split();
    for d in range(int(aux_1[1])):
        tempo_comp[n] += int(lista_aux[d]);
        
for n in range(numero):
    for d in range(numero-1):
        if tempo_comp[d] > tempo_comp[d+1]:
            aux = tempo_comp[d];
            tempo_comp[d] = tempo_comp[d+1];
            tempo_comp[d+1] = aux;
            
            aux2 = result_comp[d];
            result_comp[d] = result_comp[d+1];
            result_comp[d+1] = aux2;
            
print(result_comp[0]);
