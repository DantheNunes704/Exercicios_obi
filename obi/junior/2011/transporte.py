aux_1 = [];
aux_1 = input().split(); # os três números que representam as dimensões dos container serão dispostos
# em uma lista que será usada para calculos futuros

aux_2 = [];
aux_2 = input().split(); # o mesmo acontece com a lista que armazenará as informações do navio

largura_transporte = int(int(aux_2[0]) / int(aux_1[0])); # calcula-se a área dos containers (unidade)
comprimento_transporte = int(int(aux_2[1]) / int(aux_1[1])); # calcula-se a área do navio
# note que primeiro será feito o calculo da área bidimensional dos dois elementos
quant_container_altura = int(int(aux_2[2])/int(aux_1[2])); # calcula-se quantos containers podem ser dispostos
# pelo eixo z (altura) do navio

transporte_volume = largura_transporte * comprimento_transporte * quant_container_altura;
container_volume = int(aux_1[0]) * int(aux_1[1]) * int(aux_1[2]);



quant_containers_possiveis = int(transporte_volume / container_volume); # finalmente, calcula-se quantos
# containers podem ser dispostos pelo navio como um todo. Isso acontece ao multiplicar a quantidade de 
# containers que vão ser dispostos através do eixo Z e a área (área * altura = volume)

print(quant_containers_possiveis) # o resultado é mostrado

