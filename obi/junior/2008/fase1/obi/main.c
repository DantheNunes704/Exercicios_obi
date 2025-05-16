#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N, P, resultado = 0;

int main()
{
    scanf("%d %d", &N, &P);
    int lista[N];
    for(int n = 0; n < N; n++)
        {
            int X, Y;
            scanf("%d %d", &X, &Y);
            lista[n] = X + Y;
            if(lista[n] >= P)
            {
                resultado += 1;
            }
        }

    printf("%d", resultado);

    return 0;
}
