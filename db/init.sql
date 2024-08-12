CREATE TABLE store_delivery (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(20) NOT NULL,
    is_private BOOLEAN NOT NULL,
    is_incomplete BOOLEAN NOT NULL,
    last_purchase DATE,
    average_ticket DECIMAL(12, 2),
    ticket_last_purchase DECIMAL(12, 2),
    frequent_store VARCHAR(20),
    store_last_purchase VARCHAR(20),
    is_valid_cpf BOOLEAN NOT NULL,
    is_valid_frequent_store BOOLEAN NOT NULL,
    is_valid_store_last_purchase BOOLEAN NOT NULL
);
