letra = input() # letra que será usada

texto = input().split(" ") # "texto" se torna uma lista em que os seus elementos são strings da frase principal

quant_letra = 0 # quantidade de palavras que contém a letra especificada

for n in texto: # a variável n recebe o valor de cada elemento (palavra da frase principal) que está presente na lista
    for d in n: # a variável d recebe cada caractere da palavra contida na variável n
        if(d == letra): # verifica se a palavra contém a letra
            quant_letra += 1
            break
            # Se contém, a variável "quant_letra recebe 1 e a execução sai do escopo do segundo laço de repetição"

# isso ocorre até que todas as palavras da lista forem verificadas

reposta = round(((quant_letra/len(texto)) * 100), 1) # a resposta será o valor arredondado de uma porcentagem, da qual a mesma representa a quantidade de
# palavras na lista que contém a letra

print(reposta) # a resposta é mostrada
