tipo = "graduação"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 4, 
    "obrigatorio": True
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 2, 
    "obrigatorio": False
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 0, 
    "obrigatorio": False
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
    "creditos": 6, 
    "obrigatorio": False
    }

disciplinas_gCC = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_gCC:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_gCC = sum(listaCreditos)

saida_gCC = (f"Curso: 'Ciencia da Computação'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_gCC += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_gCC += (f"]\ncréditos obrigatórios: {creditos_gCC}")

retorno_gCC = [saida_gCC, creditos_gCC, tipo]