tipo = "doutorado"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 4, 
    "obrigatorio": False
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 0, 
    "obrigatorio": False
    }
disc5 = {
    "descricao": "Tópicos Avançados em Bancos de Dados", 
    "creditos": 4, 
    "obrigatorio": False
    }
disc6 = {
    "descricao": "Metodologia Científica", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc7 = {
    "descricao": "Tópicos Avançados em Linguagens de Programação", 
    "creditos": 4, 
    "obrigatorio": True
    }

disciplinas_dCC = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_dCC:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_dCC = sum(listaCreditos)

saida_dCC = (f"Curso: 'Ciência da Computação'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_dCC += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_dCC += (f"]\ncréditos obrigatórios: {creditos_dCC}")

retorno_dCC = [saida_dCC, creditos_dCC, tipo]