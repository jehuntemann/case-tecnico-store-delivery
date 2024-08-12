def run(file, db_connection):
    for line in file.readlines()[1:]:
        cpf, private, incomplete, last_purchase, average_ticket, ticket_last_purchase, frequent_store, store_last_purchase = line.split()
        cpf = _just_numbers(cpf)
        frequent_store = _just_numbers(frequent_store)
        store_last_purchase = _just_numbers(store_last_purchase)
        average_ticket = average_ticket.replace(",", ".")
        ticket_last_purchase = ticket_last_purchase.replace(",", ".")
        is_valid_cpf = _validate_cpf(cpf)

        if last_purchase != 'NULL':
            last_purchase = f"'{last_purchase}'"

        db_connection.query(f"INSERT INTO store_delivery (cpf, is_private, is_incomplete, last_purchase, "
                            f"average_ticket, ticket_last_purchase, frequent_store, store_last_purchase, "
                            f"is_valid_cpf, is_valid_frequent_store, is_valid_store_last_purchase) "
                            f"VALUES ('{cpf}', '{private}', '{incomplete}', {last_purchase}, {average_ticket}, "
                            f"{ticket_last_purchase}, {frequent_store}, {store_last_purchase}, {is_valid_cpf}, "
                            f"'0', '0')")

    db_connection.commit()


def _validate_cpf(cpf):
    if len(cpf) != 11:
        return False

    sum_digits = 0
    new_cpf = cpf[:-2]

    for index, digit in enumerate(new_cpf, 1):
        sum_digits += index * int(digit)
    dig_10 = sum_digits % 11

    if dig_10 > 9:
        dig_10 = 0

    new_cpf += str(dig_10)

    sum_digits = 0

    for index, digit in enumerate(new_cpf):
        sum_digits += index * int(digit)
    dig_11 = sum_digits % 11

    if dig_11 > 9:
        dig_11 = 0

    new_cpf += str(dig_11)

    if new_cpf[-2:] == cpf[-2:]:
        return True
    return False


def _just_numbers(field):
    return field.replace('.', '').replace('-', '').replace('/', '')
