import psycopg2

def transfer_data():
    try:
        source_conn = psycopg2.connect(
            dbname="source_db",
            user="source_user",
            password="123",
            host="localhost",
            port="5455"
        )
        
        target_conn = psycopg2.connect(
            dbname="target_db",
            user="target_user",
            password="123",
            host="localhost",
            port="5456"
        )

        source_cur = source_conn.cursor()
        target_cur = target_conn.cursor()

        source_cur.execute("SELECT * FROM customers;")
        customers = source_cur.fetchall()
        for customer in customers:
            target_cur.execute("INSERT INTO customers (id, name, email, phone, created_at) VALUES (%s, %s, %s, %s, %s);", customer)

        source_cur.execute("SELECT * FROM orders;")
        orders = source_cur.fetchall()
        for order in orders:
            target_cur.execute("INSERT INTO orders (id, customer_id, product_name, quantity, order_date) VALUES (%s, %s, %s, %s, %s);", order)

        target_conn.commit()

        print("Veri aktarımı başarılı.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Veri aktarımı sırasında hata oluştu:", error)

    finally:
        if source_conn:
            source_cur.close()
            source_conn.close()
        if target_conn:
            target_cur.close()
            target_conn.close()

if __name__ == '__main__':
    transfer_data()
