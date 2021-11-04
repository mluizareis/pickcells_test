tipo = "mestrado"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 4, 
    "obrigatorio": False
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 4, 
    "obrigatorio": False
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 6, 
    "obrigatorio": True
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 6, 
    "obrigatorio": False
    }
disc5 = {
    "descricao": "Tópicos Avançados em Bancos de Dados", 
    "creditos": 0, 
    "obrigatorio": False
    }
disc6 = {
    "descricao": "Metodologia Científica", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc7 = {
    "descricao": "Tópicos Avançados em Linguagens de Programação", 
    "creditos": 6, 
    "obrigatorio": True
    }

disciplinas_mIC = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_mIC:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_mIC = sum(listaCreditos)

saida_mIC = (f"Curso: 'Inteligência Computacional'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_mIC += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_mIC += (f"]\ncréditos obrigatórios: {creditos_mIC}")

retorno_mIC = [saida_mIC, creditos_mIC, tipo]