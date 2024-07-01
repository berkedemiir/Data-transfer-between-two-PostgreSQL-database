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

        source_cur.execute("SELECT id, name, email, phone, created_at FROM customers;")
        customers = source_cur.fetchall()

        for customer in customers:
            id, name, email, phone, created_at = customer
            full_name = name  
            contact_email = email
            phone_number = phone
            joined_date = created_at

            target_cur.execute("""
                INSERT INTO clients (client_id, full_name, contact_email, phone_number, joined_date)
                VALUES (%s, %s, %s, %s, %s);
            """, (id, full_name, contact_email, phone_number, joined_date))

        target_conn.commit()
        print("Veri aktarımı başarıyla tamamlandı!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Hata: {error}")

    finally:
        if source_cur:
            source_cur.close()
        if target_cur:
            target_cur.close()
        if source_conn:
            source_conn.close()
        if target_conn:
            target_conn.close()

if __name__ == "__main__":
    transfer_data()
