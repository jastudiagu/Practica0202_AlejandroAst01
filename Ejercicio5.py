G = "Gryffindor"
S = 'Slytherin'

nombre= (input('Escribe tu nombre: '))
sexo = input('¿Eres chico o chica? Contesta "M" si chico o "F" si chica: ')

s = sexo.upper()
n = nombre.upper()

if (n[0] < 'M') and (s == 'F'):
    print('Perteneces a Gryffindor.')
elif (n[0] > 'N') and (s == 'M'):
    print('Perteneces a Gryffindor.')
else:
    print('Perteneces a Slytherin')