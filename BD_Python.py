import psycopg2

with psycopg2.connect(database="netology_db", user="postgres", password="1111") as con:
    conn = con
      
def create():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            customers_id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            surname VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
            phones_id SERIAL PRIMARY KEY,
            number CHAR(11) NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS customers_phones(
            customers_id INTEGER REFERENCES customers (customers_id),
            phones_id INTEGER REFERENCES phones (phones_id),
            CONSTRAINT pkae PRIMARY KEY (customers_id, phones_id)
        );
        """)
        conn.rollback()
    
def add_customers(customers_id, name, surname, email):
    with conn.cursor() as cur:
        cur.execute(f"""
        INSERT INTO customers(customers_id, name, surname, email) VALUES({customers_id}, '{name}', '{surname}', '{email}');
        """)

def add_phone(phones_id, number):
    with conn.cursor() as cur:
        cur.execute(f"""
        INSERT INTO phones(phones_id, number) VALUES({phones_id}, {number});
        """)

def add_customers_phones(customers_id, phones_id):
    with conn.cursor() as cur:
        cur.execute(f"""
        INSERT INTO customers_phones(customers_id, phones_id) VALUES({customers_id}, {phones_id});
        """)

def change_customers_name(customers_id, name):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE customers SET name=%s WHERE customers_id=%s;
        """, (customers_id, name))
        cur.execute("""
        SELECT * FROM customers;
        """)
        print(cur.fetchall())

def change_customers_surname(customers_id, surname):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE customers SET surname=%s WHERE customers_id=%s;
        """, (customers_id, surname))
        cur.execute("""
        SELECT * FROM customers;
        """)
        print(cur.fetchall()) 

def change_customers_email(customers_id, email):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE customers SET email=%s WHERE customers_id=%s;
        """, (customers_id, email))
        cur.execute("""
        SELECT * FROM customers;
        """)
        print(cur.fetchall()) 

def change_phone(phones_id, number):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE phones SET number=%s WHERE phones_id=%s;
        """, (phones_id, number))
        cur.execute("""
        SELECT * FROM phones;
        """)
        print(cur.fetchall()) 

def del_phone(phones_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM customers_phones WHERE phones_id=%s;
        """, (phones_id))
        cur.execute("""
        SELECT * FROM customers_phones;
        """)
        cur.execute("""
        DELETE FROM phones WHERE phones_id=%s;
        """, (phones_id))
        cur.execute("""
        SELECT * FROM phones;
        """)
        print(cur.fetchall())

def del_customers(customers_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM customers_phones WHERE customers_id=%s;
        """, (customers_id))
        cur.execute("""
        SELECT * FROM customers_phones;
        """)
        cur.execute("""
        DELETE FROM customers WHERE customers_id=%s;
        """, (customers_id))
        cur.execute("""
        SELECT * FROM customers;
        """)
        print(cur.fetchall())

def search_customers(name, surname, email):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM customers WHERE name LIKE %s OR surname LIKE %s OR email LIKE %s;
        """, (name, surname, email))
        print(cur.fetchone())

# В ЗАВИСИМОСТИ ОТ ЗАПРОСА УБИРАЕМ КОММЕНТИРОВАНИЕ С НУЖНЫХ ПОЗИЦИЙ

#name = input('Введите имя: ')
#surname = input('Введите фамилию: ')
#email = input('Введите имейл: ')
#number = input('Введите номер телефона: ')
#customers_id = input('Введите ID покупателя: ')
#phones_id = input('Введите ID номера: ')

#create()
#add_customers(customers_id, name, surname, email)
#add_phone(phones_id, number)
#add_customers_phones(customers_id, phones_id)
#change_customers_name(customers_id, name)
#change_customers_surname(customers_id, surname)
#change_customers_email(customers_id, email)
#change_phone(phones_id, number)
#del_phone(phones_id)
#del_customers(customers_id)
#search_customers(name, surname, email)


    
