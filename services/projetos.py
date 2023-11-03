from models.Projeto import Projeto
from repository.projetoRepository import projetoRepository


class ProjetosController:
  def getProjetos():
    try:
      pr = projetoRepository()
      projetos = pr.select()
      return projetos
    except Exception as exception:
      raise

  def addProjeto(p):
    try:
      pr = projetoRepository()
      pr.insert(p)
    except Exception as exception:
      raise
    

  def getLastProjeto():
    try:
      pr = projetoRepository()
      lastp = pr.getLastProjeto()
      return lastp
    except Exception as exception:
      raise