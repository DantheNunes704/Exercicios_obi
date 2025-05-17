aux_1 = [];
aux_1 = input().split(); # os três números que representam as dimensões dos contêineres serão dispostos
# em uma lista que será usada para calculos futuros

aux_2 = [];
aux_2 = input().split(); # o mesmo acontece com a lista que armazenará as informações do navio

largura_transporte = int(int(aux_2[0]) / int(aux_1[0])); # calcula-se quantos contêineres podem ser dispostos considerando a largura do navio
comprimento_transporte = int(int(aux_2[1]) / int(aux_1[1])); # calcula-se quantos contêineres podem ser dispostos considerando o comprimento do navio
quant_container_altura = int(int(aux_2[2])/int(aux_1[2])); # calcula-se quantos containêres podem ser dispostos considerando a altura do navio

quant_containers_possiveis = transporte_volume = largura_transporte * comprimento_transporte * quant_container_altura; # finalmente, calcula-se quantos
# contêiners podem ser dispostos pelo navio como um todo. Isso acontece ao multiplicar a quantidade de 
# contêiners que vão ser dispostos através do eixo Z e através da largura e comprimento do navio

print(quant_containers_possiveis) # o resultado é mostrado

