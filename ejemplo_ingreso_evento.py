
accion_uno = "Ya estoy en la entrada al evento"
accion_dos = "Me estoy registrando"



#Estructura de control (condicional o sentencia if o si)
#Permite continuar un flujo(realizar algo) si cumple una condicion y en caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa)
# esta sentencia (condicional if) va acompañado de los operadores de comparacion

'''
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno != estructura_datos_dos
'''

#Hay varias maneras de utilizar la sentencia if
#if simple, if compuesto, if anidado

#if simple
'''
dato_comparacion = 18
edad = 20
'''

'''
if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
'''

'''
#if compuesto
if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")
'''

'''
boleta = True
fecha_evento = "28-02-2023"
fecha_comparacion = "28-02-2023"
#if anidado
if edad
'''


#localidad de las boletas
dato_comparacion = 18
edad = 13
boleta = True

localidades = '''
1- VIP
2- Preferencial
3- General
4- Baja
'''
print(localidades)

op = int (input("Que voleta quiere adquirir"))
if op is 1:
    print("El precio es:$", 100000)

elif op is 2:
    print("El precio es:$", 75000)

elif op is 3:
    print("El precio es:$", 50000)

elif op is 4:
    print("El precio es:$", 30000)
    

'''
#No funciona el codigo
int (input("Que boleta quiere adquirir" ))
(input("Ingrese su edad"))
if edad >= dato_comparacion and boleta:
    print("Ingrese y disfrute del evento")
else:
    print("No puede ingresar")



if localidades == 1 and edad >= dato_comparacion and boleta:
    print("La localidad de su boleta es VIP")
if localidades == 2 and edad >= dato_comparacion and boleta:
    print("La localidad de su boleta es Preferencial")
if localidades == 3 and edad >= dato_comparacion and boleta:
    print("La localidad de su boleta es General")
if localidades == 4 and edad >= dato_comparacion and boleta:
    print("La localidad de su boleta es Baja")
if localidades <1 or localidades >4:
    print("Esta localidad no existe")
'''