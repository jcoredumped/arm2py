### Parte Lexica, TOKENS

#reserved es un diccionario para reservar las palabras del lenguaje y darle
#prioridad palabra : TOKEN

reserved = {
        'GLOBAL' : 'GLOBAL',
        'global' : 'global',
        'TEXT' : 'TEXT',
        'text' : 'TEXT',
        'B':'B',
        'b' : 'B',
        'BEQ' : 'BEQ',
        'beq' : 'BEQ',
        'BNE' : 'BNE',
        'bne' : 'BNE',
        'BHI' : 'BHI',
        'bhi' : 'BHI',
        'BLS' : 'BLS',
        'bls' : 'BLS',
        'BGE' : 'BGE',
        'bge' : 'BGE',
        'BLT' : 'BLT',
        'blt' : 'BLT',
        'BGT' : 'BGT',
        'bgt' : 'BGT',
        'BLE': 'BLE',
        'ble' : 'BLE',
        'AND' : 'AND',
        'and' : 'AND',
        'ORR' : 'ORR',
        'orr' : 'ORR',
        'EOR' : 'EOR',
        'eor' : 'eor',
        'add' : 'ADD',
        'ADD' : 'ADD',
        'SUB' : 'SUB',
        'sub' : 'SUB',
        'RSB' : 'RSB',
        'rsb' : 'RSB',
        'MOV' : 'MOV',
        'mov' : 'MOV',
        'cmp' : 'CMP',
        'CMP' : 'CMP',
        'MUL' : 'MUL',
        'mul' : 'MUL',
        'MLA' : 'MLA',
        'mla' : 'MLA',
        'LDR' : 'LDR',
        'ldr' : 'LDR',
        }
tokens =(
        
        #Directivas
        
        'GLOBAL',   # Directiva global (.global start)
        'TEXT',     # Directiva text (Indica inicio de instrucciones)
        'DATA',     # Directiva data
        'BSS',      # Directiva bss
        'WORD',     # Directiva word
        'SPACE',    # Directiva space
        'EQU',      # Directiva equ
        'END',      # Directiva end (Indica final del programa)
        
        # Registro

        'REGISTRO',       # Registros, posible problema pq son del tipo r0,pc...  es decir, no son estilo MIPS $0... tocara implementarlo como token funcion


        #Caracteres
        
        'COMA',      # ,
        'DP',        # :
        'IGUAL',     # =
        'CA',        # [
        'CC',        # ]
        'PUNTO',     # .
        'FL',         # Saltos de linea \n
        'ALMOADILLA', # #
        #Enteros
        
        'ENTERO',       # Entero positivo
        'ENTERONEGATIVO',      # Entero negativo
        'DIRHEXA',      # 0x11
        
        # etiqueta
        'ETIQUETA',


        #Instrucciones AL

        'AND',     # AND
        'ORR',     # OR
        'EOR',     # XOR
        'ADD',     # SUMA
        'SUB',     # RESTA
        'RSB',     # Resta inversa
        'MOV',      # mover a registro
        'CMP',      # comparar dos registros

        #Instrucciones multiplicacion
        
        'MUL',        # Multiplicacion
        'MLA',        # Multiplicacion mas incremento

        #Instrucciones memoria (load y store)
        
        'LDR',         # Load to reg
        'STR',          # Store to mem

        #Instrucciones de salto

        'B',           # Salto incondicional
        'BEQ',         # salto igual
        'BNE',         # salto distinto
        'BHI',         # salto mayor que (sin signo)
        'BLS',         # salto menor o igual que (sin signo)
        'BGE',         # salto mayor o igual que (sin signo)
        'BLT',         # salto menor que con signo
        'BGT',         # salto mayor que con signo
        'BLE',         # salto menor o igual que (con signo)
        )


# tokens a ignorar

t_ignore = ' \t'
t_ignore_COMMENT = r'\@.*'



# Implementacion de los tokens de directivas

def t_GLOBAL (t):
    'global|GLOBAL'
    return t

def t_TEXT (t): 
    r'text|TEXT'
    return t

def t_DATA (t): 
    r'DATA|data'
    return t

def t_BSS (t): 
    r'bss|BSS'
    return t
def t_WORD (t):
    r'word|WORD'
    return t

def t_SPACE (t):
    r'space|SPACE'
    return t

def t_EQU (t):
    r'equ|EQU'
    return t

def t_END (t):
    r'end|END'
    return t

# Implementacion de los tokens de caracteres

t_COMA = r','
t_DP = r':'
t_IGUAL = r'='
t_CA = r'\['
t_CC = r'\]'
t_PUNTO = r'\.'
t_FL = r'\n+'
t_ALMOADILLA = r'\#'
# Implementacion de tokens de enteros 

t_DIRHEXA = r'0[xX][0-9A-Fa-f]{2,8}'

# token etiqueta

#t_ETIQUETA = r'[a-zA-Z][a-zA-Z0-9]*'

# tokens instrucciones AL, se deben implementar como funciones para que no lo absorva etiqueta, las funciones tienen mas prioridad

def t_ENTERO (t):
    r'[0-9]+'
    return t

def t_REGISTRO (t):
    r'(r|R)(1[0-9]|2[0-9]|3[0-1]|[0-9])'
    return t


def t_ENTERONEGATIVO (t):
    r'-[0-9]+'

def t_AND (t):
    r'AND|and'
    return t

def t_ORR (t):
    r'ORR|orr'
    return t

def t_EOR (t):
    r'EOR|eor'
    return t

def t_ADD (t):
    r'ADD|add'
    return t
def t_SUB(t):
    r'SUB|sub'
    return t
def t_RSB (t):
    r'RSB|rsb'
    return t
def t_MOV (t):
    r'MOV|mov'
    return t
def t_CMP (t):
    r'CMP|cmp'
    return t

# tokens instrucciones multiplicacion

def t_MUL (t):
    r'MUL|mul'
    return t

def t_MLA (t):
    r'MLA|mla'
    return t

# tokens instrucciones memoria

def t_LDR (t):
    r'LDR|ldr'
    return t

def t_STR (t):
    r'STR|str'
    return t

# tokens instrucciones de salto


def t_BEQ (t):
    r'BEQ|beq'
    return t

def t_BNE (t):
    r'BNE|bne'
    return t

def t_BHI (t):
    r'BHI|bhi'
    return t

def t_BLS (t):
    r'BLS|bls'
    return t

def t_BGE (t):
    r'BGE|bge'
    return t

def t_BLT (t):
    r'BLT|blt'
    return t

def t_BGT (t):
    r'BGT|bgt'
    return t

def t_BLE (t):
    r'BLE|ble'
    return t

def t_B (t):
    r'B|b'
    return t

def t_ETIQUETA(t):
  r'[a-zA-Z][a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'ETIQUETA')
  return t

# funcion en caso de error lexico

def t_error (t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


def debugLEX(ficheroARM):
    salida=""
    try:
        fichero=open(ficheroARM, 'r')
        for linea in fichero:
            salida += linea

        fichero.close()
    except IOError:
        print "El fichero no existe"
    return salida



import ply.lex as lex

lexer = lex.lex()

lexer.input(debugLEX('probarLexico.txt'))

while True:
    tok = lexer.token()
    if not tok: break
    if tok.type != 'FL':
      print tok.type,
    else:
        print tok.type
