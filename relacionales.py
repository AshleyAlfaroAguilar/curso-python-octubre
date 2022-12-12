# == igual que 
from traceback import print_tb


color = 'azul'
print(color=='azul')
print(color=='rojo')

# != diferente que 
print(color!='rojo')

# > mayor que 
altura = 150
altura_minima = 150
print(altura>altura_minima)

# < menor que 
print(altura<altura_minima)

# >=
print(altura>= altura_minima)

precio = 100 
IVA = 0.12
impuesto = precio *  IVA
print(impuesto)

# <= menor o igual
print( altura<=altura_minima)

def abrir_puerta(altura,edad):
    ALTURA_MINIMA = 150
    EDAD_MINIMA = 15
    EDAD_MAXIMA= 80

    if altura <= ALTURA_MINIMA:
        print('no alcanza')
        return

    if edad<= EDAD_MINIMA:
        print('muy joven')
        return

    if edad>=EDAD_MAXIMA:
        print('Muy grande')
        return
        
    print('pase adelante')
           
           
abrir_puerta(140,14)