balas_produz = int(input());
balas = [];
menor = 0;

balas = input().split(" ");


for n in range(balas_produz-1):
    if n == 0:
        menor = int(balas[n]);
    
    if int(balas[n+1]) < menor:
        menor = int(balas[n+1]);
        
print(menor);

