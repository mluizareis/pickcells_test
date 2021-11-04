tipo = "doutorado"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 4, 
    "obrigatorio": False
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 6, 
    "obrigatorio": False
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 2, 
    "obrigatorio": True
    }
disc5 = {
    "descricao": "Tópicos Avançados em Bancos de Dados", 
    "creditos": 2, 
    "obrigatorio": False
    }
disc6 = {
    "descricao": "Metodologia Científica", 
    "creditos": 6, 
    "obrigatorio": True
    }
disc7 = {
    "descricao": "Tópicos Avançados em Linguagens de Programação", 
    "creditos": 0, 
    "obrigatorio": False
    }

disciplinas_dIA = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_dIA:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_dIA = sum(listaCreditos)

saida_dIA = (f"Curso: 'Inteligência Artificial'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_dIA += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_dIA += (f"]\ncréditos obrigatórios: {creditos_dIA}")

retorno_dIA = [saida_dIA, creditos_dIA, tipo]