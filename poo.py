class Member :
    height = None
    imc = None
    name = None

    def __init__(self,  name):
        self.name = name

    def register(self):
        print('Usuario registrado')

    def welcome(self):
        print(f'Hola, bienvenido {self.name}')

rafa = Member('Rafael')

rafa.height = 172
rafa.imc = 15
print(rafa.height)
print(rafa.imc)
rafa.register()
print(type(rafa))
#rafa.name= 'Rafael'
rafa.welcome()

billy = Member('Billy')
#billy.name = 'Billy'
billy.welcome()

#herencia
class Person():
    first_name= None
    last_name = None
    birthdate = None

    def be_in_gym(self):
        print('Estoy en el gimnasio')

class Trainer(Person):
    salary = None

    def be_in_gym(self):
        print('estoy trabajando')

class Member(Person):
    imc = None

    def be_in_gym(self):
        print('Estoy ejercitandome')

alumno = Member()
alumno.be_in_gym()

persona = Person()
print(type('persona'))

from abc import ABC, abstractmethod

class Vehicle(ABC):
    doors = None
    wheels = None

    @abstractmethod
    def avanzar(self):
        pass

class Car(Vehicle):
    doors = 5 
    wheels = 4

    def avanzar(self):
        return 'Avanzo en 4 ruedas'

class Bike(Vehicle):
    doors = 0
    wheels = 2

    def avanzar(self):
        print (f'Avanzo en {self.wheels} ruedas')

    def __str__(self) -> str:
        return f'Esta es una moto con {self.doors} puertas y {self.wheels} ruedas'

    
#Vehiculo = Vehicle()
#Vehiculo.avanzar()
carro = Car()
print(carro.doors)

bike = Bike()
bike.avanzar()
print(bike)


class User():
    password = 'Contraseña-encriptada'

    def __init__(self) -> None:
        self.password = self.__decrypt()

    def __decrypt(self):
        return 'Contraseña-desencriptada'

usuario = User()
print(usuario.password)


