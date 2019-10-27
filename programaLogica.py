
import random
#Matriz de referencia

#Funcion para obtener el último elemento agregado a las operacions
negacion = {'0':'1', 
            '1':'0', 
            '2':'2'}

conjuncion = {'00':'0',  #o
               '01':'0', 
               '02':'0',
               '10':'0', 
               '11':'1', 
               '12':'1',
               '20':'0', 
               '21':'1', 
               '22':'1'}

def top(op):
    if (len(op)==0):
        return "-" #Caracter invalido
    else:
        return op[len(op)-1]
#Funcion para ver precedencia
def precedencia(op):
    if(op in "*+=") :
      return 1
    elif(op in "n") :
      return 2            
    else:
      return 0

def evaluar(expresion):
    e = 0
    while (len(expresion) != 1):
        if (expresion[e] == "+"):
            v = expresion[e-2:e]
            expresion = expresion[:e-2] + conjuncion[v] + expresion[e+1:]
            e=0
        if (expresion[e] == "="):
            v = expresion[e-2]
            v = negacion[v]
            v = v + expresion[e-1]
            expresion = expresion[:e-2] + conjuncion[v] + expresion[e+1:]
            e=0
        if (expresion[e] == "n"):
            v = expresion[e-1]
            expresion = expresion[:e-1] + negacion[v] + expresion[e+1:]
            e=0
        else:
            e+=1
    return expresion

def independencia(resultado):
    respuesta = True
    comparacion = resultado.pop()
    for i in resultado:
        if (comparacion != i):
            respuesta = False
    return respuesta

def operar(expresion):
    #Limpiar la expresion de espacios
    expresion = expresion.replace(' ','')
    #Staxks de  expresiones y cadena resultante
    num = ""
    op = []
    resultado=[]
    #Conversion a postfix
    for c in expresion:
        if (c in "xyz"):
            num = num + c
        elif (c in "n("):
            op.append(c)  
        elif (c in ")"):
            while (top(op) != "("):
                num = num + op.pop() 
            op.pop()
        elif (c in "*+="):
            if precedencia(c) >= precedencia(top(op)): 
                op.append(c)  
            else: 
                while (not(precedencia(c) < precedencia(top(op)))):
                    num = num + op.pop()  
        else:
            print('Error', c)

    while (len(op) != 0):
        num = num + op.pop() 
    #Asigancion de tamaño
    zVueltas = 3 if ("z" in num) else 1
    yVueltas = 3 if ("y" in num) else 1
    xVueltas = 3 if ("x" in num) else 1
    #Evalaucion de la expresion 
    for z in range(zVueltas):
        for y in range(yVueltas):
            for x in range(xVueltas):
                #Sustitucion de valores
                numAc = num.replace('x',str(x))
                numAc = numAc.replace('y',str(y))
                numAc = numAc.replace('z',str(z))
                resultado.append(evaluar(numAc))
    return independencia(resultado)

def axiomas():
    s = ["(x+x)=x","x=(x+y)","(x+y)=(y+x)","(x=y)=((z+x)=(z+y))"]
    return s


cont = 0
for i in range(3**9):
    n = i
    r = 0
    s = []
    for j in range(8, -1, -1):
        r = n // (3**j)
        s.append(str(r))
        n = n-(r * (3**j))
    print(s)
    #if(funcion(s)):
    #    break
    conjuncion = {str(i)+str(j) :s.pop() for i in range(3) for j in range(3)}
    values = []
    for z in range(3):
            for y in range(3):
                for x in range(3):
                    cont += 1
                    values.append(str(x))
                    values.append(str(y))
                    values.append(str(z))
    for l in range(27) :
        negacion = ({str(k) : values.pop() for k in range(3)})
        cont+=1
        #print(negacion, conjuncion)
        if (operar("(x+x)=x") and operar("x=(x+y)") and operar("(x+y)=(y+x)") and operar("(x=y)=((z+x)=(z+y))") and not(operar("(nx)=(x=y)"))):
            #print(negacion,conjuncion)
            break
print(cont)

#print(s)

#print(operar("(x+x)=x"))

#Ingreso de la expresion infix
"""
print("(x+x)=x",operar("(x+x)=x"))
print("x=(x+y)",operar("x=(x+y)"))
print("(x+y)=(y+x)",operar("(x+y)=(y+x)"))
print("(x=y)=((z+x)=(z+y))",operar("(x=y)=((z+x)=(z+y))"))"""
#evaluar(expresion)

# Generacion aleatoria de valores
"""
values = []
for z in range(3):
        for y in range(3):
            for x in range(3):
                values.append(str(z))
                values.append(str(y))
                values.append(str(x))

for l in range(9) :
    print ({str(l//3)+str(l%3) : values.pop() for i in range(3) for j in range(3)}) 
""" 
#print ({str(k) : j for k in range(3)}) #negacion
"""
#print ({str(i)+str(j) : random.randint(0, 2) for i in range(3) for j in range(3)}) # o

"""