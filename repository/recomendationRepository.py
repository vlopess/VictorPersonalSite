import os
import pathlib
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])



from database.configs.connection import DBConnectionHandler
from models.Dica import Dica


class recomendationRepository:
    def select(self):
        with DBConnectionHandler() as db:
            cur = db.getCursor()
            cur.execute("SELECT * FROM Dica;")
            results = cur.fetchall()
            dicas = []
            for result in results:
                    dica = Dica(result[0], result[1],result[2],result[3])
                    dicas.append(dica)
            return dicas


    def insert(self, dica : Dica):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("INSERT INTO DICA (URL, DESCRICAO, IMAGE_URL, TIPO) VALUES (%s, %s, %s, %s)", (dica.url, dica.texto, dica.image_url, dica.tipo))
                db.commitar()
            except Exception as exception:
                db.session.rollback()
                raise exception
            


