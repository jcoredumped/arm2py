import string 
from instMIPS import *
etiq= {} 
programa= {} 
memoria= {} 
registros= {}
for i in range(32): 
	registros[i]= 0
pc= 1
direc=string.atoi('0X00A0000F' , 16)
etiq['datos']=direc
memoria[direc]= 24 
direc=direc + 4
memoria[direc]= 15 
direc=direc + 4
programa[1]='ila(pc, registros, etiq, 16, "datos")'
programa[2]='ilw(pc, registros, memoria, 17, 0, 16)'
programa[3]='ilw(pc, registros, memoria, 17, 4, 16)'
programa[4]='iadd(pc,registros, 19, 17, 18)'
posfinal= 5

while pc != posfinal: 
	pc= eval(programa[pc])
imprime_res(registros, memoria)
