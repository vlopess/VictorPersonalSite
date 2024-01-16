import os
import pathlib
import sys

from models.Projeto import Projeto

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])



from database.configs.connection import DBConnectionHandler


class projetoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("SELECT * FROM Projeto;")
                results = cur.fetchall()
                projetos = []
                for result in results:
                        projeto = Projeto(result[2],result[1])
                        projetos.append(projeto)
                return projetos
            except Exception as exception:
                raise exception


    def insert(self, projeto : Projeto):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("INSERT INTO PROJETO (ID,URL, DESCRICAO) VALUES ((SELECT COUNT(ID) FROM PROJETO)+1, %s, %s)", (projeto.url, projeto.name))
                db.commitar()
            except Exception as exception:
                raise exception
            
    def getLastProjeto(self):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("SELECT * FROM PROJETO")
                results = cur.fetchall()
                if len(results) == 0:
                    return None
                result = results[0]
                projeto = Projeto(result[2], result[1])
                return projeto
            except Exception as exception:
                raise exception
