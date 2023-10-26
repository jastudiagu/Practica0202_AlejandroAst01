n = int(input('Escribe un número entero: '))

if n <0:
    n = -n

for i in range(1,n+1):
    for j in range(n+1):
        print(i * n)

