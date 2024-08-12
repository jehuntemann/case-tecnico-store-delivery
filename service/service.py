def run(file, db_connection):
    for line in file.readlines()[1:]:
        cpf, private, incomplete, last_purchase, average_ticket, ticket_last_purchase, frequent_store, store_last_purchase = line.split()
        cpf = _just_numbers(cpf)
        frequent_store = _just_numbers(frequent_store)
        store_last_purchase = _just_numbers(store_last_purchase)
        average_ticket = average_ticket.replace(",", ".")
        ticket_last_purchase = ticket_last_purchase.replace(",", ".")

        if last_purchase != 'NULL':
            last_purchase = f"'{last_purchase}'"

        db_connection.query(f"INSERT INTO store_delivery (cpf, is_private, is_incomplete, last_purchase, "
                            f"average_ticket, ticket_last_purchase, frequent_store, store_last_purchase, "
                            f"is_valid_cpf, is_valid_frequent_store, is_valid_store_last_purchase) "
                            f"VALUES ('{cpf}', '{private}', '{incomplete}', {last_purchase}, {average_ticket}, "
                            f"{ticket_last_purchase}, {frequent_store}, {store_last_purchase}, '0', "
                            f"'0', '0' )")

    db_connection.commit()


def _just_numbers(field):
    return field.replace('.', '').replace('-', '').replace('/', '')
