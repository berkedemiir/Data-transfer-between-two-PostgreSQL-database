import psycopg2

def transfer_data():
    try:
        # Connect to source database
        source_conn = psycopg2.connect(
            dbname="source_db",
            user="source_user",
            password="source_password",
            host="localhost",
            port="5455"
        )

        # Connect to target database
        target_conn = psycopg2.connect(
            dbname="target_db",
            user="target_user",
            password="target_password",
            host="localhost",
            port="5456"
        )

        source_cur = source_conn.cursor()
        target_cur = target_conn.cursor()

        # Fetch data from source database
        source_cur.execute("SELECT * FROM customers;")
        customers = source_cur.fetchall()

        # Insert data into target database
        for customer in customers:
            target_cur.execute("INSERT INTO customers (id, name, email, phone, created_at) VALUES (%s, %s, %s, %s, %s);", customer)

        target_conn.commit()
        print("Data transfer completed successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

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
