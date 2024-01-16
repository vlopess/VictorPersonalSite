import os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])
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