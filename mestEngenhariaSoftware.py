tipo = "mestrado"

disc1 = {
    "descricao": "Algoritmos e Programação", 
    "creditos": 4, 
    "obrigatorio": True
    }
disc2 = {
    "descricao": "Matemática Computacional", 
    "creditos": 6, 
    "obrigatorio": False
    }
disc3 = {
    "descricao": "Estatística",  
    "creditos": 6, 
    "obrigatorio": True
    }
disc4 = {
    "descricao": "Empreendedorismo e Inovação", 
    "creditos": 0, 
    "obrigatorio": False
    }
disc5 = {
    "descricao": "Tópicos Avançados em Bancos de Dados", 
    "creditos": 4, 
    "obrigatorio": True
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

disciplinas_mES = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

listaDescricao = []
listaCreditos = []

for x in disciplinas_mES:
    if x.get("obrigatorio") == True: 
        listaDescricao.append(x.get("descricao"))
        listaCreditos.append(x.get("creditos"))

creditos_mES = sum(listaCreditos)

saida_mES = (f"Curso: 'Engenharia de Software'\n"
+f"Disciplinas: [\n")

for x in range(0, len(listaDescricao)):
    saida_mES += ("\t{\n"+
    f"\tdescrição: {listaDescricao[x]},\n\tcréditos: {listaCreditos[x]}\n"
    +"\t},\n")

saida_mES += (f"]\ncréditos obrigatórios: {creditos_mES}")

retorno_mES = [saida_mES, creditos_mES, tipo]