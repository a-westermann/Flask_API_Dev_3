import psycopg2
from connect import Connect
import names


def insert(environment: str, cmds: list[str]) -> bool:
    db_connection = Connect(environment)
    connection = db_connection.conn
    cursor = db_connection.cursor
    for cmd in cmds:
        cursor.execute(cmd)
    connection.commit()
    connection.close()
    return True


def select(environment: str, query: str):
    db_connection = Connect(environment)
    connection = db_connection.conn
    cursor = db_connection.cursor
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results



# testing stuff
def insert_names():
    inserts = []
    for n in open('names/name_list').readlines():
        clean_name = n.strip()
        sql = f"INSERT INTO name_list (name) VALUES ('{clean_name}');"
        inserts.append(sql)
    success = insert('postgresql', inserts)




if __name__ == '__main__':
    insert_names()
    results = select('postgresql', "Select * from name_list;")
    print(results)