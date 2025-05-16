#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char lista[];
int main()
{
    scanf("%s", &lista);



    int resp[strlen(lista)];

    for(int n = 0; n < strlen(lista); n++)
        {
            switch (lista[n]){
            case 'a':
                resp[n] = 2;
                break;
            case 'b':
                resp[n] = 2;

            case 'c':
                resp[n] = 2;

            case 'd':
                resp[n] = 3;

            case 'e':
                resp[n] = 3;
            case 'f':
                resp[n] = 3;

            case 'g':
                resp[n] = 4;

            case 'h':
                resp[n] = 4;

            case 'i':
                resp[n] = 4;

            case 'j':
                resp[n] = 5;
            case 'k':
                resp[n] = 5;
            case 'l':
                resp[n] = 5;
                case 'm':
                resp[n] = 6;
            case 'n':
                resp[n] = 6;
            case 'o':
                resp[n] = 6;

            case 'p':
                resp[n] = 7;
            case 'q':
                resp[n] = 7;
            case 'r':
                resp[n] = 7;

            case 's':
                resp[n] = 7;

            case 't':
                resp[n] = 8;

            case 'u':
                resp[n] = 8;

            case 'v':
                resp[n] = 8;

            case 'w':
                resp[n] = 9;

            case 'x':
                resp[n] = 9;
            case 'y':
                resp[n] = 9;
            case 'z':
                resp[n] = 9;
            }

            for(int n = 0; n < strlen(lista); n++)
                {
                    printf("%d", resp[n]);
                }




        }


    return 0;
}
