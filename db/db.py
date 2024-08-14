import psycopg2
import logging
logger = logging.getLogger(__name__)


class MyDatabase():
    def __init__(self, host="db",
                 database="postgres",
                 user="postgres",
                 password="postgres"):
        self.conn = None
        self.cur = None
        try:
            logger.info('Connecting on database')
            self.conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)
            self.cur = self.conn.cursor()
            logger.info('Connected on database successfully')
        except Exception as e:
            logger.error(e)

    def query(self, query):
        self.cur.execute(query)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
