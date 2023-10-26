frase = input('Escribe una frase: ')
frase_analizada = frase.upper()
letra = input('Escribe una letra: ')
letra_analizada = letra.upper()
fl = len(frase)
cont = 0

for i in range(0, fl):
    if frase_analizada[i] == letra_analizada:
        cont = cont +1


print('La letra {} está {} veces'.format(letra,cont))