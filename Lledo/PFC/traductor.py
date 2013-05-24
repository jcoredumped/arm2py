
#@author: lledo


tokens = ( 'REG', 'ENT', 'ENTN', 
           'DIRHEX',  
           'COMA', 'SL', 'PA', 'PC', 'DP', 
           'DDATA', 'DWORD', 'DSPACE', 'DTEXT', 'DEND', 
           'IADD', 'IADDI', 'ISUB', 'IAND', 'IANDI', 'IOR', 'IORI', 'ISLL', 'ILW', 'ISW', 'IBEQ', 'IBNE', 'IJ', 
           'ILI', 'ILA', 'IBGE', 'IBGEZ', 'IBGT', 'IBGTZ', 'IBLE', 'IBLEZ', 'IBLT', 'IBLTZ', 'ETIQ',
           'ISLT', 'ISLTI', 'ISEQ', 'ISGE', 'ISGT', 'ISLE', 'ISNE'
          )


t_COMA    =r','
t_SL      =r'\n+'
t_PA      =r'\('
t_PC      =r'\)'
t_DP      =r'\:'

t_DDATA   =r'\.data|\.DATA'
t_DWORD   =r'\.word|\.WORD'
t_DSPACE  =r'\.space|\.SPACE'
t_DTEXT   =r'\.text|\.TEXT'
t_DEND    =r'\.end|\.END'


t_REG     =r'\$([12]?[0-9]|3[01])|[rR]0|[vV][01]|[aA][0-3]|[tT][0-9]|[sS][0-8]|[kK][01]|gp|GP|sp|SP|[rR]a'


t_DIRHEX  =r'0[xX][0-9A-Fa-f]{8}'
t_ENT     =r'[0-9]+'
t_ENTN    =r'-[0-9]+'
t_ETIQ    =r'[a-zA-Z][a-zA-Z0-9]*'


t_ignore= ' \t'
t_ignore_COMMENT =r'\#.*'
    
def t_IADDI (t):   
    r'addi|ADDI'
    return t

def t_IADD (t):    
    r'add|ADD'
    return t

def t_ISUB (t):    
    r'sub|SUB'
    return t

def t_IANDI (t):   
    r'andi|ANDI'
    return t

def t_IAND (t):    
    r'and|AND'
    return t

def t_IORI (t):    
    r'ori|ORI'
    return t

def t_IOR (t):     
    r'or|OR'
    return t

def t_ISLL (t):   
    r'sll|SLL'
    return t

def t_ILW (t):     
    r'lw|LW'
    return t

def t_ISW (t):     
    r'sw|SW'
    return t

def t_IBEQ (t):    
    r'beq|BEQ'
    return t

def t_IBNE (t):    
    r'bne|BNE'
    return t

def t_IJ (t):      
    r'j|J'
    return t


def t_ILI (t):     
    r'li|LI'
    return t

def t_ILA (t):     
    r'la|LA'
    return t

def t_IBGEZ (t):    
    r'bgez|BGEZ'
    return t

def t_IBGE (t):    
    r'bge|BGE'
    return t

def t_IBGTZ (t):    
    r'bgtz|BGTZ'
    return t

def t_IBGT (t):    
    r'bgt|BGT'
    return t

def t_IBLEZ (t):    
    r'blez|BLEZ'
    return t

def t_IBLE (t):    
    r'ble|BLE'
    return t

def t_IBLTZ (t):    
    r'bltz|BLTZ'
    return t

def t_IBLT (t):    
    r'blt|BLT'
    return t

def t_ISLTI (t):    
    r'slti|SLTI'
    return t

def t_ISLT (t):    
    r'slt|SLT'
    return t

def t_ISEQ (t):    
    r'seq|SEQ'
    return t

def t_ISGE (t):    
    r'sge|SGE'
    return t

def t_ISGT (t):    
    r'sgt|SGT'
    return t

def t_ISLE (t):    
    r'sle|SLE'
    return t

def t_ISNE (t):    
    r'sne|SNE'
    return t


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

#final de la parte lex e inicio de yacc

salida=""
fsalida=open('salida.py', 'w')
nl=1

def p_s(p):
    's : bd bi'

    
def p_bd(p):
    '''bd : d sl bd 
            | e d sl bd 
            | e DTEXT sl 
            | DTEXT sl
            | sl bd'''


def p_bi(p):
    '''bi : i sl bi
            | e i sl bi
            | end sl
            | end
            | sl bi'''


def p_e(p):
    'e : ETIQ DP'
    global salida
    salida+="\netiq['{0}']=direc".format(p[1])
    fsalida.write("\netiq['%s']=direc" % p[1])
    
def p_d_word(p):
    '''d : DWORD enteros 
          | space '''

    
def p_d_data(p):
    'd : DDATA DIRHEX'
    global salida
    salida+= "\ndirec=string.atoi('{0}', 16)".format(p[2])
    fsalida.write("\ndirec=string.atoi('%s' , 16)" % p[2])
    
def p_enteros(p):
    '''enteros : ENTN COMA enteros 
                | ENT COMA enteros 
                | ENT 
                | ENTN'''
    global salida
    salida+="\nmemoria[direc]= {0}\ndirec=direc + 4".format(p[1])
    fsalida.write("\nmemoria[direc]= %s \ndirec=direc + 4" % p[1])
 
def p_space_ent(p):
    'space : DSPACE ENT'
    global salida
    salida+="\nfor i in range/{0}: \n\tmemoria[direc]=direc + 4".format(p[2])
    fsalida.write("\nfor i in range/%s: \n\tmemoria[direc]=direc + 4" % p[2])

def p_space(p):
    'space : DSPACE'
    global salida
    salida+="\nmemoria[direc]=0 \ndirec= direc + 4"
    fsalida.write("\nmemoria[direc]=0 \ndirec=direc + 4")
    
def p_sl(p):
    '''sl : SL sl 
            | SL'''

    
def p_i_add(p):
    'i : IADD REG COMA REG COMA REG'
    global l
    global salida
    salida+="\nprograma[{0}]='iadd(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='iadd(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1

def p_i_addi(p):
    'i : IADDI REG COMA REG COMA ENT'
    global nl
    global salida
    salida+="\nprograma[{0}]='iaddi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    fsalida.write("\nprograma[{0}]='iaddi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    nl=nl+1
    
def p_i_sub(p):
    'i : ISUB REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='isub(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='isub(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_and(p):
    'i : IAND REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='iand(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='iand(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_andi(p):
    'i : IANDI REG COMA REG COMA ENT'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iandi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida= salida + "\nprograma[", nl, "]='iandi(pc, registros,", numero(p[2]), ",", numero(p[4]), ",", p[6], ")'"
    nl=nl+1
    
def p_i_or(p):
    'i : IOR REG COMA REG COMA REG'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ior(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    salida+="\nprograma[{0}]='ior(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    nl=nl+1
    
def p_i_ori(p):
    'i : IORI REG COMA REG COMA ENT'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iori(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='iori(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_sll(p):
    'i : ISLL REG COMA REG COMA ENT'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='isll(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='isll(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_lw(p):
    'i : ILW REG COMA ENT PA REG PC'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ilw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6])))
    salida+="\nprograma[{0}]='ilw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6]))
    nl=nl+1
    
def p_i_sw(p):
    'i : ISW REG COMA ENT PA REG PC'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='isw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6])))
    salida+="\nprograma[{0}]='isw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6]))
    nl=nl+1
    
def p_i_beq(p):
    'i : IBEQ REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibeq(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='ibeq(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_bne(p):
    'i : IBNE REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibne(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='ibne(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_j(p):
    'i : IJ ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ij(etiq, %s)'".format(p[2]))
    salida+="\nprograma[{0}]='ij(etiq, %s)'".format(p[2]) 
    nl=nl+1
    
def p_i_li(p):
    'i : ILI REG COMA ENT'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ili(pc, registros, {1}, {2})'".format(nl, numero(p[2]), p[4]))
    salida+="\nprograma[{0}]='ili(pc, registros, {1}, {2})'".format(nl, numero(p[2]), p[4])
    nl=nl+1
    
def p_i_la(p):
    'i : ILA REG COMA ETIQ'
    global nl, i
    global salida
    fsalida.write("\nprograma[{0}]='ila(pc, registros, etiq, {1}, \"{2}\")'".format(nl, numero(p[2]), p[4]))
    salida+="\nprograma[{0}]='ila(pc, registros, etiq, {1}, \"{2}\")'".format(nl, numero(p[2]), p[4])
    nl=nl+1
    
    
def p_i_bge(p):
    'i : IBGE REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibge(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='ibge(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_bgez(p):
    'i : IBGEZ REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibgez(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6]))
    salida+="\nprograma[{0}]='ibgez(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6])
    nl=nl+1
    
def p_i_bgt(p):
    'i : IBGT REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibgt(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='ibgt(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_bgtz(p):
    'i : IBGTZ REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibgtz(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6]))
    salida+="\nprograma[{0}]='ibgtz(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6])
    nl=nl+1
    
def p_i_ble(p):
    'i : IBLE REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ible(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='ible(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_blez(p):
    'i : IBLEZ REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iblez(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6]))
    salida+="\nprograma[{0}]='iblez(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6])
    nl=nl+1
    
def p_i_blt(p):
    'i : IBLT REG COMA REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iblt(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='iblt(pc, registros, etiq, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_bltz(p):
    'i : IBLTZ REG COMA ETIQ'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ibltz(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6]))
    salida+="\nprograma[{0}]='ibltz(pc, registros, etiq, {1}, {3})'".format(nl, numero(p[2]), p[6])
    nl=nl+1
    
def p_i_addi_entn(p):
    'i : IADDI REG COMA REG COMA ENTN'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iaddi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='iaddi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_andi_entn(p):
    'i : IANDI REG COMA REG COMA ENTN'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iandi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='iandi(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_ori_entn(p):
    'i : IORI REG COMA REG COMA ENTN'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='iori(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    salida+="\nprograma[{0}]='iori(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    nl=nl+1
    
def p_i_lw_entn(p):
    'i : ILW REG COMA ENTN PA REG PC'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ilw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6])))
    salida+="\nprograma[{0}]='ilw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6]))
    nl=nl+1
    
def p_i_sw_entn(p):
    'i : ISW REG COMA ENTN PA REG PC'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='isw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6])))
    salida+="\nprograma[{0}]='isw(pc, registros, memoria, {1}, {2}, {3})'".format(nl, numero(p[2]), p[4], numero(p[6]))
    nl=nl+1
    
def p_i_li_entn(p):
    'i : ILI REG COMA ENTN'
    global nl
    global salida
    fsalida.write("\nprograma[{0}]='ili(pc, registros, {1}, {2})'".format(nl, numero(p[2]), p[4]))
    salida+="\nprograma[{0}]='ili(pc, registros, {1}, {2})'".format(nl, numero(p[2]), p[4])
    nl=nl+1

def p_i_slt(p):
    'i : ISLT REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='islt(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='islt(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1

def p_i_slti(p):
    'i : ISLTI REG COMA REG COMA ENT'
    global nl
    global salida
    salida+="\nprograma[{0}]='islti(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6])
    fsalida.write("\nprograma[{0}]='islti(pc, registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), p[6]))
    nl=nl+1
    
def p_i_seq(p):
    'i : ISEQ REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='iseq(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='iseq(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_sge(p):
    'i : ISGE REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='isge(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='isge(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_sgt(p):
    'i : ISGT REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='isgt(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='isgt(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_sle(p):
    'i : ISLE REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='isle(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='isle(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1
    
def p_i_sne(p):
    'i : ISNE REG COMA REG COMA REG'
    global nl
    global salida
    salida+="\nprograma[{0}]='isne(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6]))
    fsalida.write("\nprograma[{0}]='isne(pc,registros, {1}, {2}, {3})'".format(nl, numero(p[2]), numero(p[4]), numero(p[6])))
    nl=nl+1

def p_end(p):
    'end : DEND'
    global salida
    fsalida.write("\nposfinal= %d\n" % nl)
    salida+="\nposfinal={0}\n".format(nl)

def p_error(p):
    print "Syntax error at '%s'" % p

def numero(t):
    if t=='$0' or t=='r0' or t=='R0':
        return 0
    if t=='$1' or t=='at' or t=='AT':
        return 1
    if t=='$2' or t=='v0' or t=='V0':
        return 2
    if t=='$3' or t=='v1' or t=='V1':
        return 3
    if t=='$4' or t=='a0' or t=='A0':
        return 4
    if t=='$5' or t=='a1' or t=='A1':
        return 5
    if t=='$6' or t=='a2' or t=='A2':
        return 6
    if t=='$7' or t=='a3' or t=='A3':
        return 7
    if t=='$8' or t=='t0' or t=='T0':
        return 8
    if t=='$9' or t=='t1' or t=='T1':
        return 9
    if t=='$10' or t=='t2' or t=='T2':
        return 10
    if t=='$11' or t=='t3' or t=='T3':
        return 11
    if t=='$12' or t=='t4' or t=='T4':
        return 12
    if t=='$13' or t=='t5' or t=='T5':
        return 13
    if t=='$14' or t=='t6' or t=='T6':
        return 14
    if t=='$15' or t=='t7' or t=='T7':
        return 15
    if t=='$16' or t=='s0' or t=='S0':
        return 16
    if t=='$17' or t=='s1' or t=='S1':
        return 17
    if t=='$18' or t=='s2' or t=='S2':
        return 18
    if t=='$19' or t=='s3' or t=='S3':
        return 19
    if t=='$20' or t=='s4' or t=='S4':
        return 20
    if t=='$21' or t=='s5' or t=='S5':
        return 21
    if t=='$22' or t=='s6' or t=='S6':
        return 22
    if t=='$23' or t=='s7' or t=='S7':
        return 23
    if t=='$24' or t=='t8' or t=='T8':
        return 24
    if t=='$25' or t=='t9' or t=='T9':
        return 25
    if t=='$26' or t=='k0' or t=='K0':
        return 26
    if t=='$27' or t=='k1' or t=='K1':
        return 27
    if t=='$28' or t=='gp' or t=='GP':
        return 28
    if t=='$29' or t=='sp' or t=='SP':
        return 29
    if t=='$30' or t=='s8' or t=='s8':
        return 30
    if t=='$31' or t=='ra' or t=='RA':
        return 31

import ply.yacc as yacc
yacc.yacc()

miPrograma=""


fsalida.write("import string \nfrom instMIPS import *")
fsalida.write("\netiq= {} \nprograma= {} \nmemoria= {} \nregistros= {}")
fsalida.write("\nfor i in range(32): \n\tregistros[i]= 0")
fsalida.write("\npc= 1")
salida+="import string \nfrom instMIPS import *"
salida+="\netiq = {} \nprograma= {} \nmemoria= {} \nregistros= {}\nfor i in range(32): \n\tregistros[i]= 0"
salida+="\npc=1"
try:
    fentrada=open('mips.txt', 'r')
    
    i=1
    for linea in fentrada:
        miPrograma=miPrograma + linea
        i=i+1
    fentrada.close()
except IOError:
    print "El fichero no existe"

yacc.parse(miPrograma)
fsalida.write("\nwhile pc != posfinal: \n\tpc= eval(programa[pc])")
fsalida.write("\nimprime_res(registros, memoria)\n")
fsalida.close()
salida+="\nwhile pc != posfinal: \n\tpc= eval(programa[pc])\nimprime_res(registros, memoria)\n"

print salida
exec salida

    
