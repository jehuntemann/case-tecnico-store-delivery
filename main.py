from db import db
import sys
from service import service
from datetime import datetime


def main():
    if len(sys.argv) <= 1:
        print('Faltou passar arquivo por parâmetro')

    else:
        print(f'lendo arquivo "{sys.argv[1]}"')
        try:
            arquivo = sys.argv[1]
            with open(arquivo, 'r+') as file:
                db_connection = db.MyDatabase()
                service.run(file, db_connection)
                db_connection.close()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    tic = datetime.now()
    main()
    tac = datetime.now()
    print('%s', (tac-tic))
