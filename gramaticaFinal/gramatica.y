%{
#include <stdio.h>
int ln=1;
%}
%union{
    int tipoi;
    char *string;
}
%token <string> DIRHEXA
%token <string> ETIQUETA
%token <tipoi> ENTERO
%token <tipoi> ENTERONEGATIVO
%token <tipoi> REGISTRO
%token GLOBAL DATA WORD EQU BSS SPACE TEXT END
%token AND ORR EOR ADD SUB RSB MOV CMP 
%token MUL MLA 
%token LDR STR
%token B BEQ BNE BHI BLS BGE BLT BGT BLE
%token DP PUNTO IGUAL CA CC COMA ALMOADILLA FL
%%
s:  resto sig1
 | sig1
 ;
sig1: global resto sig2
    ;
global: PUNTO GLOBAL ETIQUETA
      ;
sig2: PUNTO DATA resto listazonadata
    | sig3
    ;
listazonadata: tipodata listazonadata
             | tipodata sig3
             ;
             
tipodata: equ rzd
        | word listaword resto
        ;
rzd: ENTERO  resto 
   | ENTERONEGATIVO  resto 
   | DIRHEXA  resto 
   ;

equ: PUNTO EQU ETIQUETA COMA
   ;
word: ETIQUETA DP PUNTO WORD
    ;
listaword: DIRHEXA COMA listaword
         | ENTERO COMA listaword
         | ENTERONEGATIVO COMA listaword
         | DIRHEXA
         | ENTERO
         | ENTERONEGATIVO
         ;
sig3: PUNTO BSS  resto listazonabss sig4
    | sig4
    ;
listazonabss: ETIQUETA DP PUNTO SPACE enterohexa resto listazonabss 
            | ETIQUETA DP PUNTO SPACE enterohexa resto
       ;
//space: ETIQUETA DP PUNTO SPACE
  //   ;
enterohexa: ENTERO
       | DIRHEXA
       ;
sig4: PUNTO TEXT  resto inst  resto
    ;
inst: ETIQUETA DP resto inst
    | ETIQUETA DP instruccion  resto inst
    | instruccion  resto inst
    | fin
    ;

instruccion: AND REGISTRO COMA REGISTRO COMA regoinm
           | ORR REGISTRO COMA REGISTRO COMA regoinm
           | EOR REGISTRO COMA REGISTRO COMA regoinm
           | ADD REGISTRO COMA REGISTRO COMA regoinm
           | SUB REGISTRO COMA REGISTRO COMA regoinm
           | RSB REGISTRO COMA REGISTRO COMA regoinm
           | MOV REGISTRO COMA regoinm
           | CMP REGISTRO COMA regoinm
           | MUL REGISTRO COMA REGISTRO COMA REGISTRO
           | MLA REGISTRO COMA REGISTRO COMA REGISTRO
           | LDR REGISTRO COMA CA REGISTRO COMA regoinm CC
           | LDR REGISTRO COMA CA REGISTRO CC
           | STR REGISTRO COMA CA REGISTRO COMA regoinm CC
           | STR REGISTRO COMA CA REGISTRO CC
           | LDR REGISTRO COMA IGUAL ETIQUETA
           | LDR REGISTRO COMA ETIQUETA
           | STR REGISTRO COMA ETIQUETA
           | B etiquetaoentero
           | BEQ etiquetaoentero
           | BNE etiquetaoentero
           | BHI etiquetaoentero
           | BLS etiquetaoentero
           | BGE etiquetaoentero
           | BLT etiquetaoentero
           | BGT etiquetaoentero
           | BLE etiquetaoentero
           ;
etiquetaoentero: ETIQUETA
               | PUNTO reoe
               ;
							 
reoe: ENTERO 
    | ENTERONEGATIVO 
    | DIRHEXA 
    ;

regoinm: REGISTRO
       | ALMOADILLA DIRHEXA
       | ALMOADILLA ENTERO
       | ALMOADILLA ENTERONEGATIVO
       ;
fin: ETIQUETA DP B PUNTO  resto PUNTO END
   | B PUNTO resto PUNTO END 
   ;

resto: FL{ln++;}  resto 
     | FL{ln++;}  
     ;

%%
int main() {
  yyparse();

}

yyerror(s) char *s;

{printf("\nError de sintaxis en la linea %d\n", ln);}
