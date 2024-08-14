import logging
logger = logging.getLogger(__name__)


def execute(file, db_connection):
    logger.info('Starting data process')
    for line in file.readlines()[1:]:
        cpf, private, incomplete, last_purchase_date, average_ticket, ticket_last_purchase, frequent_store, \
            store_last_purchase = line.split()
        cpf = _just_numbers(cpf)
        frequent_store = _just_numbers(frequent_store)
        store_last_purchase = _just_numbers(store_last_purchase)
        average_ticket = average_ticket.replace(",", ".")
        ticket_last_purchase = ticket_last_purchase.replace(",", ".")
        is_valid_cpf = _validate_cpf(cpf)
        is_valid_frequent_store = _validate_cnpj(frequent_store)
        is_valid_store_last_purchase = _validate_cnpj(store_last_purchase)

        if last_purchase_date != 'NULL':
            last_purchase_date = f"'{last_purchase_date}'"

        db_connection.query(f"INSERT INTO store_delivery (cpf, is_private, is_incomplete, last_purchase_date, "
                            f"average_ticket, ticket_last_purchase, frequent_store, store_last_purchase, "
                            f"is_valid_cpf, is_valid_frequent_store, is_valid_store_last_purchase) "
                            f"VALUES ('{cpf}', '{private}', '{incomplete}', {last_purchase_date}, {average_ticket}, "
                            f"{ticket_last_purchase}, {frequent_store}, {store_last_purchase}, {is_valid_cpf}, "
                            f"{is_valid_frequent_store}, {is_valid_store_last_purchase})")

    db_connection.commit()
    logger.info('Process finished successfully')

def _validate_cpf(cpf):
    if len(cpf) != 11:
        return False

    new_cpf = cpf[:-2]
    for start in (1, 0):
        sum_digits = 0
        for index, digit in enumerate(new_cpf, start):
            sum_digits += index * int(digit)
        dig = sum_digits % 11

        if dig > 9:
            dig = 0
        new_cpf += str(dig)

    if new_cpf == cpf:
        return True
    return False


def _validate_cnpj(cnpj):
    if len(cnpj) != 14:
        return False

    new_cnpj = cnpj[:-2]
    multi = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(new_cnpj) < 14:
        sum_digits = 0
        for index, digit in enumerate(new_cnpj):
            sum_digits += multi[index] * int(digit)
        dig = sum_digits % 11
        if dig <= 1:
            dig = 0
        else:
            dig = 11 - dig
        new_cnpj += str(dig)
        multi.insert(0, 6)

    if new_cnpj == cnpj:
        return True
    return False


def _just_numbers(field):
    return field.replace('.', '').replace('-', '').replace('/', '')
