contraseña = input('Escribe aquí tu contraseña: ')
pregunta = input('¿Cúal es la contraseña que has puesto?: ')

validar_contraseña = contraseña.upper()
validar = pregunta.upper()

if validar == validar_contraseña:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')