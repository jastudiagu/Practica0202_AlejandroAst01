print ('Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.')
edad = int(input('Escribe tu edad: '))
im = float(input('Escribe tus ingresos mensuales: '))

if (edad >= 16) and (im >= 1000):
    print('Tienes que tributar. ')
else:
    print('No tienes que tributar. ')