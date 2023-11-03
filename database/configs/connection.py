import psycopg2

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "host='localhost' dbname='WebSite' user='postgres' password='admin'"
        self.__connection = psycopg2.connect(self.__connection_string)

    def __enter__(self):
        return self

    def getCursor(self):
        return self.__connection.cursor()
    def commitar(self):
        return self.__connection.commit()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.cursor().close()
        self.__connection.close()

