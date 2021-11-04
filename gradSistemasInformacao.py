tipo = "graduação"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 4, 
    "obrigatorio": False
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 0, 
    "obrigatorio": False
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 4, 
    "obrigatorio": True
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 4, 
    "obrigatorio": True
    }
disc5 = {
    "descricao": "Tópicos Avançados em Bancos de Dados", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc6 = {
    "descricao": "Metodologia Científica", 
    "creditos": 4, 
    "obrigatorio": True
    }
disc7 = {
    "descricao": "Tópicos Avançados em Linguagens de Programação", 
    "creditos": 4, 
    "obrigatorio": True
    }

disciplinas_gSI = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_gSI:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_gSI = sum(listaCreditos)

saida_gSI = (f"Curso: 'Sistemas de Informação'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_gSI += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_gSI += (f"]\ncréditos obrigatórios: {creditos_gSI}")

retorno_gSI = [saida_gSI, creditos_gSI, tipo]