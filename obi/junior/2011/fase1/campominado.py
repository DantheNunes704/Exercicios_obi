tabuleiro = [];
numero = int(input());
resposta = [];

for n in range(numero):
    resposta.append(0);

for n in range(numero):
    tabuleiro.append(int(input()));
    
for n in range(numero):
    if n == 0 and n == numero-1:
        if tabuleiro[n] == 1:
            resposta[n] += 1;
    elif n == 0:
        if tabuleiro[n] == 1:
            resposta[n] += 1;
        if tabuleiro[n+1] == 1:
            resposta[n] += 1;
    elif n == numero-1:
        if tabuleiro[n] == 1:
            resposta[n] += 1;
        if tabuleiro[n-1] == 1:
            resposta[n] += 1;
    else:
         if tabuleiro[n] == 1:
            resposta[n] += 1;
         if tabuleiro[n+1] == 1:
            resposta[n] += 1;
         if tabuleiro[n-1] == 1:
            resposta[n] += 1;
           
for n in range(numero):
    print(resposta[n]);

     
          
