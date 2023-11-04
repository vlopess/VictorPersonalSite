import psycopg2

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "host='dpg-cl32h12uuipc7385fpg0-a.oregon-postgres.render.com' dbname='victorpersonal_database' user='victorpersonal_database_user' password='HU9p0LWKdsjm4nZI5LenFGOioVWgZizY'"
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

#postgres://victorpersonal_database_user:HU9p0LWKdsjm4nZI5LenFGOioVWgZizY@dpg-cl32h12uuipc7385fpg0-a.oregon-postgres.render.com/victorpersonal_database