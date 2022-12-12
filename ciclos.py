numero =1 

while numero <=10:
    print(numero)
    numero +=1

perros = ['bobby', 'rex','max', 'avellana']
for perro in perros:
    print(perro)

numero=1
while numero <=10:
    if numero==5:
        break 

    print(numero)
    numero +=1

perros = ['bobby', 'rex','max', 'avellana']
for perro in perros:
    if perro =='max':
        print('este si es el perro')
        continue

    print('este no es el perro')