import os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])



from database.configs.connection import DBConnectionHandler


class passwordRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                cur = db.getCursor()
                cur.execute("SELECT * FROM PASSWORD;")
                results = cur.fetchall()
                map = {}
                for result in results:
                        map[result[0]] = result[1]
                return map
            except Exception as exception:
                raise exception
