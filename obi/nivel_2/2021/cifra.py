alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z'];

palavra = [];

palavra = list(input());
palavra_fim = [];

vogais = ['a', 'e', 'i', 'o', 'u'];

for n in range(len(palavra)):
    if vogais.count(palavra[n]) == 0:
        palavra_fim.append(palavra[n]);
        posicao = alfabeto.index(palavra[n]);
        
        for d in range(posicao, len(alfabeto)):
            for num_aux in range(1, len(alfabeto)):
                if d - num_aux >= 0 and vogais.count(alfabeto[d-num_aux]) == 1:
                    palavra_fim.append(alfabeto[d-num_aux]);
                    break;
                elif d + num_aux < len(alfabeto) and vogais.count(alfabeto[d+num_aux])  == 1:
                    palavra_fim.append(alfabeto[d+num_aux]);
                    break;
            break;
        
        for d in range(posicao, len(alfabeto)):
            for num_aux in range(1, len(alfabeto)):
                if d - num_aux >= 0 and vogais.count(alfabeto[d+num_aux]) == 0:
                    palavra_fim.append(alfabeto[d+num_aux]);
                    break;
            break;
    else:
        palavra_fim.append(palavra[n]);
palavra_fim_def = ''.join(palavra_fim);

print(palavra_fim_def);
