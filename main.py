from db import db
import sys
from service import service
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) <= 1:
        logger.info('Missing file parameter')

    else:
        logger.info(f'Reading file "{sys.argv[1]}"')
        try:
            arquivo = sys.argv[1]
            with open(arquivo, 'r+') as file:
                db_connection = db.MyDatabase()
                service.execute(file, db_connection)
                db_connection.close()

        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    tic = datetime.now()
    main()
    tac = datetime.now()
    print('%s', (tac-tic))
