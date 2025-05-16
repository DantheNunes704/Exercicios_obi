questoes = int(input());
quant_pontos = 0;

gabarito = [];
provaAluno = [];

gabarito = list(input());
provaAluno = list(input());

for n in range(questoes):
    if gabarito[n] == provaAluno[n]:
        quant_pontos += 1;
        
print(quant_pontos);
    