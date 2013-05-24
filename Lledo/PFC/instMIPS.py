#Lledo Villalonga Agut


def iadd(pc, registros, rd, rs, rt):
    registros[rd]=registros[rs]+registros[rt]
    return pc+1


def iaddi(pc, registros, rd, rs, inm):
    registros[rd]=registros[rs]+inm
    return pc+1


def isub(pc, registros, rd, rs, rt):
    registros[rd]=registros[rs]-regitros[rt]
    return pc+1


def iand(pc, registros, rd, rs, rt):
    registros[rd]=registros[rs]&registros[rt]
    return pc+1


def iandi(pc, registros, rd, rs, inm):
    registros[rd]=registros[rs]&inm
    return pc+1


def ior(pc, registros, rd, rs, rt):
    registros[rd]=registros[rs]|registros[rt]
    return pc+1


def iori(pc, registros, rd, rs, inm):
    registros[rd]=registros[rs]|inm
    return pc+1


def isll(pc, registros, rd, rs, desp):
    registros[rd]=registros[rs] * desp*2
    return pc+1


def ilw(pc, registros, memoria, rs, desp, rt):
    registros[rs]=memoria[registros[rt]+desp]
    return pc+1


def isw(pc, registros, memoria, rs, desp, rt):
    memoria[registros[rt]+desp]=registros[rs]
    return pc+1


def ibeq(pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]==registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)

    return pc+1


def ibne (pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]!=registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)

    return pc+1



def ij(etiq, etiqueta):
    if etiq.has_key(etiqueta):
        return etiq[etiqueta]
    else:
        print "No existe la etiqueta '", etiqueta,"'"
        return exit(0)



def ili(pc, registros, rs, inm):
    registros[rs]=inm
    return pc+1



def ila(pc, registros, etiq, rd, etiqueta):
	registros[rd] = etiq[etiqueta]
	return pc + 1


def ibge(pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]>=registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def ibgez(pc, registros, etiq, rs, etiqueta):
    if registros[rs]>=0:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def ibgt(pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]>registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def ibgtz(pc, registros, etiq, rs, etiqueta):
    if registros[rs]>0:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def ible(pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]<=registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def iblez(pc, registros, etiq, rs, etiqueta):
    if registros[rs]<=0:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1



def iblt(pc, registros, etiq, rs, rt, etiqueta):
    if registros[rs]<registros[rt]:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def ibltz(pc, registros, etiq, rs, etiqueta):
    if registros[rs]<0:
        if etiq.has_key(etiqueta):
            return etiq[etiqueta]
        else:
            print "No existe la etiqueta '", etiqueta,"'"
            return exit(0)
    return pc+1


def islt(pc, registros, rd, rs, rt):
    if registros[rs]<registros[rt]:
        registros[rd]=1
    else:
        registros[rd]=0
    return pc+1


def islti(pc, registros, rd, rs, inm):
    if registros[rs]<inm:
        registros[rd]=1
    else:
        registros[rd]=0
    return pc+1


def iseq(pc, registros, rdest, rsrc1, rsrc2):
    if registros[rsrc1]==registros[rsrc2]:
        registros[rdest]=1
    else:
        registros[rdest]=0
    return pc+1


def isge(pc, registros, rdest, rsrc1, rsrc2):
    if registros[rsrc1]>=registros[rsrc2]:
        registros[rdest]=1
    else:
        registros[rdest]=0
    return pc+1


def isgt(pc, registros, rdest, rsrc1, rsrc2):
    if registros[rsrc1]>registros[rsrc2]:
        registros[rdest]=1
    else:
        registros[rdest]=0
    return pc+1


def isle(pc, registros, rdest, rsrc1, rsrc2):
    if registros[rsrc1]<=registros[rsrc2]:
        registros[rdest]=1
    else:
        registros[rdest]=0
    return pc+1


def isne(pc, registros, rdest, rsrc1, rsrc2):
    if registros[rsrc1]!=registros[rsrc2]:
        registros[rdest]=1
    else:
        registros[rdest]=0
    return pc+1


def imprime_res(registros, memoria):
    for i in range (32):
        print "registro", i, "-->", registros[i]
    print "\nMemoria utilizada:"
    pos=memoria.items()
    pos.sort()
    for i in range (len(pos)):
        print "[",hex(pos[i][0]).upper(),"-->",pos[i][1],"]"
