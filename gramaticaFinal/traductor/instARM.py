







def initEstados():

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

# Las instrucciones aritmeticologicas tienen un parametro opcional que indica si se trata de una constante o no

######## instrucciones aritmeticas
def and (pc, registros, rd, rs, shift, constantes=0):

    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)

    registros[rd] = registros[rs] & operand #AND
    return pc + 1

def orr (pc, registros, rd, rs, shift, constantes=0):
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)
    
    registros[rd] = registros[rs] | operand # OR

    return pc + 1


def eor (pc, registros, rd, rs, shift, constantesi=0):
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)

    registros[rd] = registros[rs] ^ operand # XOR

    return pc + 1



def add (pc, registros, rd, rs, shift, constantes=0):
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)
    registros[rd] = registros[rs] + operand
    return pc + 1

def sub(pc, registros, rd, rs, shift, constantes=0):
    
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)

    registros[rd] = registros[rs] - operand
    return pc + 1

def rsb(pc, registros, rd, rs, shift, constantes=0):
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)

    registros[rd] = operand - registros[rs]
    return pc + 1

def mov(pc, registros, rd, shift, constantes=0):
    if type(constantes) == type({}): # si constantes es un diccionario es que es una constante
        operand = constantes[shift]
    elif type(shift) == type(1): # si es un entero es que es un registro
        operand = registros[shift]
    elif shift[:2] == "0X": # si es un numero en hexa
        operand = string.atoi(shift, 16)
    else: # si es un entero
        operand = string.atoi(shift)
    registros[rd] = operand    # movemos shift a registros[rd]
    return pc + 1

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


