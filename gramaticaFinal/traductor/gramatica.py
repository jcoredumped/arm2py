from lexico import tokens
import sys
import string
lineaFichero = 1

# Arbol sintactico

# s: resto sig1
#  | sig1
#  ;

def p_s(p):
    '''s : resto sig1
         | sig1
    
    '''

# sig1: global resto sig2
#     ;

def p_sig1(p):
    '''sig1 : global resto sig2 
    '''

# global: PUNTO GLOBAL ETIQUETA
#       ;

def p_global(p):
    ''' global : PUNTO GLOBAL ETIQUETA 
    '''

# sig2: PUNTO DATA resto listazonadata
#     | sig3
#     ;

def p_sig2(p):
    ''' sig2 : PUNTO DATA resto listazonadata
             | sig3
    '''

# listazonadata: tipodata listazonadata
#              | tipodata sig3
#              ;

def p_listazonadata(p):
    ''' listazonadata : tipodata listazonadata
                      | tipodata sig3
    '''

# tipodata: equ rzd
#         | word listaword resto
#         ;

def p_tipodata(p):
    ''' tipodata : equ rzd
                 | word listaword resto  
    '''

    if len(p) == 4: # si es la rama de word
        
        # Hay que hacer algo como direc
        
        print p[2]

    else: # si es un equ
        print 


# rzd: ENTERO resto
#    | ENTERONEGATIVO resto
#    | DIRHEXA resto
#    ;

def p_rzd(p):
    ''' rzd : ENTERO resto
            | ENTERONEGATIVO resto
            | DIRHEXA resto
    '''
    p[0] = p[1]

# equ: PUNTO EQU ETIQUETA COMA
#    ;

def p_equ(p):
    ''' equ : PUNTO EQU ETIQUETA COMA
    '''
    p[0] = p[3] # nos quedamos con la ETIQUETA

# word: ETIQUETA DP PUNTO WORD
#     ;

def p_word(p):
    ''' word : ETIQUETA DP PUNTO WORD
    '''

# listaword: DIRHEXA COMA listaword
#          | DIRHEXA
#          | ENTERO COMA listaword
#          | ENTERO
#          | ENTERONEGATIVO COMA listaword
#          | ENTERONEGATIVO
#          ;

def p_listaword_dirhexa(p):
    ''' listaword : DIRHEXA COMA listaword
                  | DIRHEXA
    '''
    p[0] = string.atoi(p[1], 16)

def p_listaword_entero(p):
    ''' listaword : ENTERO COMA listaword
                  | ENTERO 
    '''
    p[0] = string.atoi(p[1])

def p_listaword_enteronegativo(p):
    ''' listaword : ENTERONEGATIVO COMA listaword
                  | ENTERONEGATIVO
    '''
    p[0] = string.atoi(p[1])

# sig3: PUNTO BSS resto listazonabss sig4
#     | sig4
#     ;

def p_sig3(p):
    ''' sig3 : PUNTO BSS resto listazonabss sig4
             | sig4
    '''

# listazonabss: ETIQUETA DP PUNTO SPACE enterohexa resto listazonabss
#             | ETIQUETA DP PUNTO SPACE enterohexa resto
#

def p_listazonabss(p):
    ''' listazonabss : ETIQUETA DP PUNTO SPACE enterohexa resto listazonabss
                     | ETIQUETA DP PUNTO SPACE enterohexa resto
    '''

# enterohexa: ENTERO
#           | DIRHEXA
#           ;

def p_enterohexa_entero(p):
    ''' enterohexa : ENTERO
    '''
    p[0] = string.atoi(p[1], 16)

def p_enterohexa_dirhexa(p):
    ''' enterohexa : DIRHEXA 
    '''
    p[0] = string.atoi(p[1])

# sig4: PUNTO TEXT resto inst resto
#     ;

def p_sig4(p):
    ''' sig4 : PUNTO TEXT resto inst resto
    '''

# inst: ETIQUETA DP instruccion resto inst
#     | instruccion resto inst
#     | fin
#     ;

def p_inst(p):
    ''' inst : ETIQUETA DP resto inst
             | ETIQUETA DP instruccion resto inst
             | instruccion resto inst
             | fin
    '''


# instruccion: AND REGISTRO COMA REGISTRO COMA REGISTRO
#            | AND REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | ORR REGISTRO COMA REGISTRO COMA REGISTRO
#            | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | EOR REGISTRO COMA REGISTRO COMA REGISTRO
#            | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | ADD REGISTRO COMA REGISTRO COMA REGISTRO
#            | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | SUB REGISTRO COMA REGISTRO COMA REGISTRO
#            | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | RSB REGISTRO COMA REGISTRO COMA REGISTRO
#            | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
#            | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
#            | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
#            | MOV REGISTRO COMA REGISTRO
#            | MOV REGISTRO COMA ALMOADILLA DIRHEXA
#            | MOV REGISTRO COMA ALMOADILLA ENTERO
#            | MOV REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | MOV REGISTRO COMA ALMOADILLA ETIQUETA
#            | CMP REGISTRO COMA REGISTRO
#            | CMP REGISTRO COMA ALMOADILLA DIRHEXA
#            | CMP REGISTRO COMA ALMOADILLA ENTERO
#            | CMP REGISTRO COMA ALMOADILLA ENTERONEGATIVO
#            | MOV REGISTRO COMA ALMOADILLA ETIQUETA
#            | MUL REGISTRO COMA REGISTRO COMA REGISTRO
#            | MLA REGISTRO COMA REGISTRO COMA REGISTRO
#            | LDR REGISTRO COMA CA REGISTRO COMA REGISTRO CC
#            | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA DIRHEXA CC
#            | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERO CC
#            | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERONEGATIVO CC
#            | LDR REGISTRO COMA CA REGISTRO CC
#            | LDR REGISTRO COMA IGUAL ETIQUETA
#            | LDR REGISTRO COMA ETIQUETA
#            | STR REGISTRO COMA CA REGISTRO COMA REGISTRO CC
#            | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA DIRHEXA CC
#            | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERO CC
#            | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERONEGATIVO CC
#            | STR REGISTRO COMA CA REGISTRO CC
#            | STR REGISTRO COMA ETIQUETA
#            | B ETIQUETA
#            | B PUNTO ENTERO
#            | B PUNTO ENTERONEGATIVO
#            | B PUNTO DIRHEXA
#            | BEQ ETIQUETA
#            | BEQ PUNTO ENTERO
#            | BEQ PUNTO ENTERONEGATIVO
#            | BEQ PUNTO DIRHEXA
#            | BNE ETIQUETA
#            | BNE PUNTO ENTERO
#            | BNE PUNTO ENTERONEGATIVO
#            | BNE PUNTO DIRHEXA
#            | BHI ETIQUETA
#            | BHI PUNTO ENTERO
#            | BHI PUNTO ENTERONEGATIVO
#            | BHI PUNTO DIRHEXA
#            | BLS ETIQUETA
#            | BLS PUNTO ENTERO
#            | BLS PUNTO ENTERONEGATIVO
#            | BGE ETIQUETA
#            | BGE PUNTO ENTERO
#            | BGE PUNTO ENTERONEGATIVO
#            | BGE PUNTO DIRHEXA
#            | BLT ETIQUETA
#            | BLT PUNTO ENTERO
#            | BLT PUNTO ENTERONEGATIVO
#            | BLT PUNTO DIRHEXA
#            | BGT ETIQUETA
#            | BGT PUNTO ENTERO
#            | BGT PUNTO ENTERONEGATIVO
#            | BGT PUNTO DIRHEXA
#            | BLE ETIQUETA
#            | BLE PUNTO ENTERO
#            | BLE PUNTO ENTERONEGATIVO
#            | BLE PUNTO DIRHEXA
#            ;

def p_instruccion_and(p):
    ''' instruccion : AND REGISTRO COMA REGISTRO COMA REGISTRO
                    | AND REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | AND REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_orr(p):
    ''' instruccion : ORR REGISTRO COMA REGISTRO COMA REGISTRO
                    | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | ORR REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_eor(p):
    ''' instruccion : EOR REGISTRO COMA REGISTRO COMA REGISTRO
                    | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | EOR REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_add(p):
    ''' instruccion : ADD REGISTRO COMA REGISTRO COMA REGISTRO
                    | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | ADD REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_sub(p):
    ''' instruccion : SUB REGISTRO COMA REGISTRO COMA REGISTRO
                    | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | SUB REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_rsb(p):
    ''' instruccion : RSB REGISTRO COMA REGISTRO COMA REGISTRO
                    | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA DIRHEXA
                    | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERO
                    | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | RSB REGISTRO COMA REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_mov(p):
    ''' instruccion : MOV REGISTRO COMA REGISTRO
                    | MOV REGISTRO COMA ALMOADILLA DIRHEXA
                    | MOV REGISTRO COMA ALMOADILLA ENTERO
                    | MOV REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | MOV REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_cmp(p):
    ''' instruccion : CMP REGISTRO COMA REGISTRO
                    | CMP REGISTRO COMA ALMOADILLA DIRHEXA
                    | CMP REGISTRO COMA ALMOADILLA ENTERO
                    | CMP REGISTRO COMA ALMOADILLA ENTERONEGATIVO
                    | CMP REGISTRO COMA ALMOADILLA ETIQUETA
    '''

def p_instruccion_mul(p):
    ''' instruccion : MUL REGISTRO COMA REGISTRO COMA REGISTRO
    '''

def p_instruccion_mla(p):
    ''' instruccion : MLA REGISTRO COMA REGISTRO COMA REGISTRO
    '''

def p_instruccion_ldr(p):
    ''' instruccion : LDR REGISTRO COMA CA REGISTRO COMA REGISTRO CC
                    | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA DIRHEXA CC
                    | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERO CC
                    | LDR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERONEGATIVO CC
                    | LDR REGISTRO COMA CA REGISTRO CC
                    | LDR REGISTRO COMA IGUAL ETIQUETA
                    | LDR REGISTRO COMA ETIQUETA
    '''


def p_instruccion_str(p):
    ''' instruccion : STR REGISTRO COMA CA REGISTRO COMA REGISTRO CC
                    | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA DIRHEXA CC
                    | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERO CC
                    | STR REGISTRO COMA CA REGISTRO COMA ALMOADILLA ENTERONEGATIVO CC
                    | STR REGISTRO COMA CA REGISTRO CC
                    | STR REGISTRO COMA ETIQUETA
    '''


def p_instruccion_b(p):
    ''' instruccion : B ETIQUETA
                    | B PUNTO ENTERO
                    | B PUNTO ENTERONEGATIVO
                    | B PUNTO DIRHEXA
    '''

def p_instruccion_beq(p):
    ''' instruccion : BEQ ETIQUETA
                    | BEQ PUNTO ENTERO
                    | BEQ PUNTO ENTERONEGATIVO
                    | BEQ PUNTO DIRHEXA
    '''

def p_instruccion_bne(p):
    ''' instruccion : BNE ETIQUETA
                    | BNE PUNTO ENTERO
                    | BNE PUNTO ENTERONEGATIVO
                    | BNE PUNTO DIRHEXA
    '''

def p_instruccion_bhi(p):
    ''' instruccion : BHI ETIQUETA
                    | BHI PUNTO ENTERO
                    | BHI PUNTO ENTERONEGATIVO
                    | BHI PUNTO DIRHEXA
    '''

def p_instruccion_bls(p):
    ''' instruccion : BLS ETIQUETA
                    | BLS PUNTO ENTERO
                    | BLS PUNTO ENTERONEGATIVO
                    | BLS PUNTO DIRHEXA
    '''

def p_instruccion_bge(p):
    ''' instruccion : BGE ETIQUETA
                    | BGE PUNTO ENTERO
                    | BGE PUNTO ENTERONEGATIVO
                    | BGE PUNTO DIRHEXA
    '''

def p_instruccion_blt(p):
    ''' instruccion : BLT ETIQUETA
                    | BLT PUNTO ENTERO
                    | BLT PUNTO ENTERONEGATIVO
                    | BLT PUNTO DIRHEXA
    '''

def p_instruccion_bgt(p):
    ''' instruccion : BGT ETIQUETA
                    | BGT PUNTO ENTERO
                    | BGT PUNTO ENTERONEGATIVO
                    | BGT PUNTO DIRHEXA
    '''

def p_instruccion_ble(p):
    ''' instruccion : BLE ETIQUETA
                    | BLE PUNTO ENTERO
                    | BLE PUNTO ENTERONEGATIVO
                    | BLE PUNTO DIRHEXA
    '''


# fin: ETIQUETA DP B PUNTO resto PUNTO END
#    | B PUNTO resto PUNTO END
#    ;





def p_fin(p):
    ''' fin : ETIQUETA DP B PUNTO resto PUNTO END
            | B PUNTO resto PUNTO END
    '''




# resto: FL resto
#      | FL
#      ;

def p_resto(p):
    ''' resto : FL resto
              | FL
    '''
    global lineaFichero
    lineaFichero += 1

def p_error(p):
    print "Error de sintaxys en la linea %s" %(lineaFichero)



#### Fin del yacc








def ficheroACadena(ficheroARM):
    salida=""
    try:
      fichero=open(ficheroARM, 'r')
      for linea in fichero:
        salida += linea

      fichero.close()
    except IOError:
      print "El fichero no existe"
    return salida



import ply.yacc as yacc

parser = yacc.yacc(debug=1)


if __name__ == "__main__":



    if len(sys.argv) == 2:
        programa = ficheroACadena(sys.argv[1])
        parser.parse(programa)
    else:
        print "Falta pasar por argumento el fichero"
        print "Usage: %s fichero" % sys.argv[0]

