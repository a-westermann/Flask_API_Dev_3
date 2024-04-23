import psycopg2
from psycopg2 import DatabaseError
from psycopg2.extras import RealDictCursor
from config import read_config


class Connect():
    def __init__(self, environment):
        config = read_config(environment)
        self.cursor = None
        self.conn = self.connect(config)

    def connect(self, config):
        try:
            connection = psycopg2.connect(database=config['database'], user=config['user'],
                                          password=config['password'], host=config['host'],
                                          port=config['port'], cursor_factory=RealDictCursor)
            # with connect(**config) as conn:
            with connection as conn:
                print('Connected to Postgres server')
                self.cursor = conn.cursor()
                return conn
        except (DatabaseError, Exception) as error:
            print(error)

if __name__ == '__main__':
    conn = Connect('postgres')
