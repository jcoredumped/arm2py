bison -yd gramatica.y && flex lexico.fl && gcc y.tab.c lex.yy.c -lfl -o gramaticaARM
