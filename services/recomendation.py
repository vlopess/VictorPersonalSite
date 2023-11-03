
import os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])
from repository.recomendationRepository import recomendationRepository

class RecomendacoesController:
  def getRecomendacoes():
    try:
      rr = recomendationRepository()
      recomendacoes = rr.select()
      return recomendacoes
    except Exception as exception:
      raise

  def addRecomendacoes(r):
    try:
      recomendacoes = recomendationRepository()
      recomendacoes.insert(r)    
    except Exception as exception:
      raise


