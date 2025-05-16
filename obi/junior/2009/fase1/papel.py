bagulho = [];
bagulho = input().split(" ");


precisa = int(bagulho[0])*int(bagulho[2]);

if precisa <= int(bagulho[1]):
    print('S');
else:
    print('N');
