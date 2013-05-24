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
etiq['o']=direc
memoria[direc]= 24 
direc=direc + 4
memoria[direc]= 15 
direc=direc + 4
while pc != posfinal: 
	pc= eval(programa[pc])
imprime_res(registros, memoria)
