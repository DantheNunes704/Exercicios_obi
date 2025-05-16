maior = int(input());
operacao = input().split();

if operacao[1] == '*':
    resultado = int(operacao[0]) * int(operacao[2]);
else:
    resultado = int(operacao[0]) + int(operacao[2]);
    
if resultado > maior:
    print("OVERFLOW");
else:
    print("OK");