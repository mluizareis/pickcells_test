from gradCienciaComputacao import retorno_gCC
from gradSistemasInformacao import retorno_gSI
from mestEngenhariaSoftware import retorno_mES
from mestInteligenciaComputacional import retorno_mIC
from doutCienciaComputacao import retorno_dCC
from doutInteligenciaArtificial import retorno_dIA

lista_cursos = [retorno_gCC, retorno_gSI, retorno_mES, retorno_mIC, retorno_dCC, retorno_dIA]
lista_creditos = [retorno_gCC[1], retorno_gSI[1], retorno_mES[1], retorno_mIC[1], retorno_dCC[1], retorno_dIA[1]]

maior_credito = max(lista_creditos)
indices = [i for i, valor in enumerate(lista_creditos) if valor == maior_credito]

lista_empate_cursos = []

if len(indices) == 1:
    print(lista_cursos[indices[0]][0])
else:
    for x in indices:
        lista_empate_cursos.append(lista_cursos[x])

    curso_principal = ""
    for x in lista_empate_cursos:
        if "doutorado" in x:
            curso_principal = x
        elif "doutorado" not in x and "mestrado" in x:
            curso_principal = x
        elif "doutorado" not in x and "mestrado" not in x:
            curso_principal = x
    print(curso_principal[0])