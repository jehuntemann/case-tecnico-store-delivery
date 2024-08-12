import psycopg2

class MyDatabase():
    def __init__(self, host="db",
                       database="postgres",
                       user="postgres",
                       password="postgres" ):
        self.conn = None
        self.cur = None
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def query(self, query):
        self.cur.execute(query)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

# db = MyDatabase()
# db.query("SELECT * FROM table;")
# db.close()


