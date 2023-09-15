import random



limite_parentesis_anidados=0

max_parentesis=0

print("Bienvenidos al generador de ejercicios de operatoria combinada")
op=[]
error=0
while op==[]:
    if error!=0:
        print("Se han elegido mal las operaciones. Intentalo nuevamente.")
    
    print("\nElige de la siguiente lista las operaciones que quieras trabajar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n")
    print("\n(Ejemplo: si queires elegir suma, multiplicación y división, debes ingresar '134')\n")
    oper = input("Ingresa tus operaciones -> ")


    if "1" in oper:
        op.append("+")
    if "2" in oper:
        op.append("-")
    if "3" in oper:
        op.append("*")
    if "4" in oper:
        op.append("/")
    error=1


cantidad_numeros = int(input("Ingresa la cantidad de números involcrados en la operación -> "))

rango_numerico = input("Ingresa el rango númerico en el formato 'a,b' -> ")

parentesis_si_no = input("¿El ejercicio incluye paréntesis? (s/n) -> ")
if parentesis_si_no.lower()=="s":
    anidados=input("¿Se permiten paréntesis anidados (uno adentro de otro)? (s/n) -> ")
    if anidados.lower()== "s":
        limite_parentesis_anidados = int(input("Elige nivel máximo de los parentesis anidados (2,3,...) -> "))
    tope_parentesis = input("¿Existe un máximo número de parentesis que te gustaría utilizar? (s/n) -> ")
    if tope_parentesis.lower()=="s":
        max_parentesis = int(input("Cuantos parentesis se incluirán como máximo? (1,2,3,4,...-> "))

rango=rango_numerico.split(",")

inf=int(rango[0])
sup=int(rango[1])

resultado=1.1
imprimir_lista=0

while not(isinstance(resultado, int) or (isinstance(resultado, float) and resultado.is_integer())):
    operaciones = op
    i = 0
    lista = []


    contador_parentesis_abiertos=0

    contador_parentesis = 0
    while i<cantidad_numeros:
        if lista == []:
            np = random.randint(0,1)
            if np==0 and contador_parentesis_abiertos<max_parentesis:
                lista.append("(")
                if imprimir_lista==1:
                    print(lista)
                contador_parentesis+=1
                contador_parentesis_abiertos+=1
                

            else:
                lista.append(random.randint(inf,sup))
                if imprimir_lista==1:
                    print(lista)
                i+=1
        else:
            if lista[-1] in range(inf,sup+1):
                if contador_parentesis==0:
                    lista.append(random.choice(operaciones))
                    if imprimir_lista==1:
                        print(lista)
                else:
                    ppn=random.randint(0,1)
                    if ppn==0:
                        lista.append(random.choice(operaciones))
                        if imprimir_lista==1:
                            print(lista)
                    elif ppn==1:
                        try:
                            if lista[-2]!="(":
                                lista.append(")")
                                if imprimir_lista==1:
                                    print(lista)
                                contador_parentesis-=1
                        except:
                            pass
                        
                    
            elif lista[-1]!=")":

                np = random.randint(0,1)
                if np==0 and contador_parentesis<limite_parentesis_anidados and contador_parentesis_abiertos<max_parentesis:
                    lista.append("(")
                    if imprimir_lista==1:
                        print(lista)
                    contador_parentesis+=1
                    contador_parentesis_abiertos+=1

                elif not lista[-1] in range(inf,sup+1):
                    lista.append(random.randint(inf,sup))
                    if imprimir_lista==1:
                        print(lista)
                    i+=1
            else:
                lista.append(random.choice(operaciones))
                if imprimir_lista==1:
                    print(lista)
    while contador_parentesis>0:
        lista.append(")")
        if imprimir_lista==1:
            print(lista)
        contador_parentesis-=1

    ejercicio=""
    if inf<0:
        n=0
        for l in lista:
            a="aaaaa"
            b="bbbbb"
            try:
                a=lista[n-1]
                b=lista[n+1]
            except:
                pass
            if l in range(inf,0): #se defe modificar esta parte, no imprime el parentesis en el caso ...,0,+,-5,)
                if  a=="(" and b==")":
                    ejercicio=ejercicio+str(l)
                else:
                    ejercicio=ejercicio+"("+str(l)+")"
            else:
                ejercicio+=str(l)
            n+=1
    else:
        for l in lista:
            ejercicio+=str(l)
    print(ejercicio)
    expresion = ejercicio
    

    try:
        resultado = eval(expresion)
        print("El resultado es:", resultado)
    except Exception as e:
        print("Error al evaluar la expresión:", e)
