contraseña = input('Escribe tu contraseña: ')

validacion = input('Escribe la contraseña: ')

while validacion != contraseña:
    validacion = input('Contraseña incorrecta, vuelve a escribir tu contraseña: ')

if validacion == contraseña:
    print('Contraseña correcta')