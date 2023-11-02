from Projeto import Projeto

projetos = []

projetos.append(Projeto('TodoList Simples em C com Integração com o Obsidian', "https://github.com/vlopess/DataStructure/tree/main/TodoList"))
projetos.append(Projeto("Similar Taste: descubra músicas e artistas semelhantes com base em suas preferências musicais.","https://github.com/vlopess/SimilarTaste"))

def getProjetos():
  return projetos

def addProjeto(p):
  projetos.append(p)

def getLastProjeto():
  return projetos[len(projetos)-1]