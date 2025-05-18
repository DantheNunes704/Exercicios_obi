quant_operacao = input();
quant_operacao = int(quant_operacao);
resposta = 0;

numero, caractere = input().split(" ");


for n in range(quant_operacao-1):
    if caractere == '/' and n == quant_operacao-1:
        numero_2 = input();
        numero_2 = int(numero_2);
        resposta = resposta / numero_2;
    elif caractere == '*' and n == quant_operacao-1:
        numero_2 = input();
        numero_2 = int(numero_2);
        resposta = resposta * numero_2;
    elif caractere == '/' and n == 0:
        numero_2, caractere = input().split();
        numero_2 = int(numero_2);
        resposta = numero / numero_2;
    elif caractere == '*' and n == 0:
        numero_2, caractere = input().split();
        numero_2 = int(numero_2);
        resposta = numero * numero_2;
    elif caractere == '*':
        numero_2, caractere = input().split();
        numero_2 = int(numero_2);
        resposta = resposta * numero_2;
    else:
        numero_2, caractere = input().split();
        numero_2 = int(numero_2);
        resposta = resposta / numero_2;

        
print(resposta);
