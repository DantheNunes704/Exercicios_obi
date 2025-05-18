mat_lin, mat_col, lin, col = int(input().split());

fazenda = [mat_lin][mat_col];

lista_aux = [];



for n in range(mat_lin*mat_col):
    lista_aux[n] = 0;

for f in range(len(lista_aux)):
    for h in range(mat_col):
        for h in range(mat_col):
            for n in range(lin):
                for d in range(col):
                    lista_aux += fazenda[n]