import math

def idademed (idade1, idade2, idade3):
    if idade1 < idade3 and idade1 > idade2 or idade1 > idade3 and idade1 < idade2 or idade1 == idade2 == idade3:
        return idade1
    elif idade2 < idade1 and idade2 > idade3 or idade2 > idade1 and idade2 < idade3:
        return idade2
    else:
        return idade3

idade1 = int(input())
idade2 = int(input())
idade3 = int(input())


print(idademed(idade1, idade2, idade3))