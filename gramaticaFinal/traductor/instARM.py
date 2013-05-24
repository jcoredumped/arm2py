

### Idea de diccionario de estados

## Un diccionario tal que la clave sea lo que representa

estados = {
        'N' : '',       #Indica ultima op dio resultado negativo N=1 o positivo N=0
        'Z' : '',      # Indica si el resultado de la op fue zero Z=1 o no Z=0
        'C' : '',     # Para suma o comparacion C=1 si hubo carry, para las operaciones de desplazamiento toma el valor del bit saliente
        'V' : '',     # V=1 indica que hubo overflow
        }


# Condiciones asociadas a las instrucciones de salto... B{sufijo}

# EQ  Igual                           Z=1
# NE Distinto                         Z=0
# HI Mayor que (sin signo)            C=1 & Z=0
# LS Menor o igual que (sin signo)    C=0 | Z=1
# GE Mayor o igual que (con signo)    N == V
# LT Menor que con signo              N != V
# GT Mayor que con signo              Z=0 & N==V
# LE Menor o igual que (con signo)    Z=1 | N != V



## Posibles ideas para solventar el problema de si es registro o inmediato:

## + Implementar funciones a parte

## + Una unica funcion y comprobar si se trata de un registro o inmediato, como en ARM los registros se nombran de una unica forma se puede implementar el diccionario de registros usando de clave la cadena del registro, entonces seria facil de distinguir numero de registro, bastaria con mirar si esta la clave del parametro

## + Mediante otro parametro que se use simplemente para diferenciar. Pero creo que seria una mala programacion.


######## instrucciones aritmeticas
def and (pc, registros, rd, rs, rt):
    
    operand=registros[rt]

    ### si rt es registro
    registros[rd] = registros[rs] & operand
    return pc + 1

def orr (pc, registros, rd, rs, rt):
    ## si rt es registro
    registros[rd] = registros[rs] | operand
    return pc + 1


def eor (pc, registros, rd, rs, rt):
    ### si rt es registro
    return pc + 1


def add (pc, registros, rd, rs, rt):
    registros[rd] = registros[rs] + registros[rt]
    return pc + 1

def sub():
    pass

def rsb():
    pass

def mov():
    pass

def cmp():
    pass


######## instrucciones de multiplicacion

def mul():
    pass

def mla():
    pass

### instrucciones de acceso a memoria

def ldr():
    pass

def str():
    pass


####### instrucciones de salto

def b():
    pass

def beq():
    pass

def bne():
    pass

def bhi():
    pass

def bls():
    pass

def bge():
    pass

def blt():
    pass

def bgt():
    pass

def ble():
    pass


