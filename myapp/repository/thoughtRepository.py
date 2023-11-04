import os
import pathlib
import sys

from models.Thought import Thought


curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])



from database.configs.connection import DBConnectionHandler


class thoughtRepository:
    def select(self):
        with DBConnectionHandler() as db:
            cur = db.getCursor()
            cur.execute("SELECT * FROM Thought ORDER BY ID DESC;")
            results = cur.fetchall()
            pensamentos = []
            for result in results:
                    texto = result[0]
                    hora = result[1]
                    time = str(hora)
                    pensamento = Thought(texto, time)
                    pensamentos.append(pensamento)
            return pensamentos


    def insert(self, pensa : Thought):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("INSERT INTO Thought (DESCRICAO, DATAPUBLICACAO, ID) VALUES (%s, %s, (SELECT COUNT(ID) FROM Thought)+1)", (pensa.texto, pensa.time))
                db.commitar()
            except Exception as exception:
                db.session.rollback()
                raise exception
            


