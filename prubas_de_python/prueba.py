#cosas de el python

print("jejej la clase esta de weba XD")

#ejemplo de while
edad = 0
while edad < 18:
    edad = edad + 1
    print("edad, tienes" + str(edad))

#ejemplo de if
print("Escribe algo: ")
entrada = input()

if entrada == "dios":
    print("Si se cuplio la condicion")
else:
    print("no se cumplio")

#ejemplo de for
secuencia = ["uno","dos","tres"]
for elemento in secuencia:
    print(elemento)

#funciones
def miFuncion(a,b):
    print(a + " "+ b)

miFuncion("hola","Mundo")