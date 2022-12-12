edad = input ('ingrese su edad\n')

if int(edad) > 18:
    print('tu eres mayor de edad')
elif int(edad)==18:
    print('tienes 18 exactos')
else:
    print ('tu eres menor de edad')


edad_parseada =  int(edad)
if edad_parseada >18:
    if edad_parseada==20:
        print('tienes 20')
    else:
        print('eres mayor de edad pero no tienes 20')

if edad_parseada>18:
    pass
else:
    print('no puedes entrar')

nombre = 'dAyAn '
if nombre.upper().strip() != 'DAYAN':
    print('que bueno que no eres dayane, bienvenido')
else:
    print('que no puedes entrar!!')
