# Ejercicio 1
# MCD
def maximo_comun_divisor(numero1,numero2):
    mcd = 1
    if numero1 == 0:
        mcd = numero2
    elif numero2 == 0:
        mcd = numero1
    else:
        for i in range(min(numero1,numero2),1,-1):
            if numero1 % i == 0 and numero2 % i == 0:
                mcd = i
                break
    return mcd

mcd = maximo_comun_divisor(51,34)
print("Ejercicio 1: El MCD es",mcd)

# Ejercicio 2
# MCM
def minimo_comun_multiplo(numero1, numero2):
    return int(numero1 * numero2 / (maximo_comun_divisor(numero1,numero2)))

mcm = minimo_comun_multiplo(51,34)
print("Ejercicio 2: El mcm es",mcm)

# Ejercicio 3
# Diccionario con palabras y frecuencia
def repeticion_palabras(cadena):
    dict = {}
    lista = cadena.split(" ")
    for i in range(len(lista)):
        palabra = lista[i]
        if lista[i] in dict:
            dict[palabra] += 1
        else:
            dict[palabra] = 1
    return(dict)

print("Ejercicio 3: Diccionario:",repeticion_palabras("hoy es un buen día para salir a comer un buen asado"))

# Ejercicio 4
# Tupla con la palabra más repetida del diccionario
def palabra_mas_repetida(cadena):
    dict = repeticion_palabras(cadena)
    clave = ""
    valor = 0
    for i in dict:
        if dict[i] > valor:
            valor = dict[i]
            clave = i
    return((clave,valor))

print("Ejercicio 4: Tupla:",palabra_mas_repetida("hoy es un buen día para salir a comer un buen asado"))

# Ejercicio 5
# Validar número en forma iterativa
def get_int_iterativa():
    while True:
        try:
            numero = int(input("Ingrese un número entero:"))
            break
        except ValueError:
            pass
    return numero

print("Ejercicio 5 Iterativo",get_int_iterativa())

# Validar número en forma recursiva
def get_int_recursiva():
    resultado = ""
    while True:
        numero = input("Ingrese un número entero:")
        resultado = val_numero(numero)
        if len(resultado) == len(numero):
            break
    return int(resultado)

def val_numero(numero):
    resultado = ""
    if len(numero) > 0 and (numero[0]).isdigit():
        resultado = numero[0] + val_numero(numero[1:len(numero)])
    return resultado

print("Ejerciaio 5 Recursivo",get_int_recursiva())

# Ejercicio 6
# Clase Persona
class Persona:
    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self,valor):
        if type(valor) != str:
            raise ValueError
        self.__nombre = valor

    @edad.setter
    def edad(self,valor):
        if type(valor) != int:
            raise ValueError
        elif valor < 0 or valor > 120:
            raise ValueError
        self.__edad = valor

    @dni.setter
    def dni(self,valor):
        try:
            if type(valor) != int:
                raise ValueError
            elif valor < 100000 or valor > 99999999:
                raise ValueError
            else:
                self.__dni = valor
        except ValueError:
            print("Dato inválido")

    def mostrar(self):
         print('Ejercicio 6:, Nombre {} - edad {} - DNI: {}'.format(self.__nombre,self.__edad,self.__dni))

    def es_mayor_de_Edad(self):
        if self.__edad__ >= 18:
            return True
        else:
            return False

p1 = Persona("Alicia",22,123456789)
p1.mostrar()

# Ejercicio 7
# Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad = 0.00):
        self.__titular = Persona(titular)
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,valor):
        self.__titular = valor

    # @cantidad.setter
    # def cantidad(self,valor):
    #     self.__cantidad = valor

    def mostrar(self):
         print('Ejercicio 7: La cuenta pertenece a {} y posee una cantidad de {}'.format(self.__titular.nombre,self.__cantidad))

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self,cantidad):
        self.__cantidad -= cantidad

c1 = Cuenta("Alicia")
c1.mostrar()
c1.ingresar(1000)
c1.retirar(200)
c1.mostrar()
c1.retirar(2000)
c1.mostrar()

# Ejercicio 8
# Cuenta Joven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0, bonificacion = 0.00):
        super().__init__(titular,cantidad)
        self.__bonificacion = bonificacion

    @property    
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,valor):
        self.__bonificacion = valor

    def es_titular_valido(self):
        if self.titular.edad >= 18 and self.titular.edad < 25:
            return True
        else:
            return False
        
    def retirar(self,cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
         print('Ejercicio 8: Cuenta Joven - Bonificación {}%'.format(self.__bonificacion))

j1 = CuentaJoven("Paula",0,10)
j1.mostrar()
j1.ingresar(1000)
j1.retirar(200)
j1.retirar(2000)
