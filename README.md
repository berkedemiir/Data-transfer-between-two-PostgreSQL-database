# Data-transfer-between-two-PostgreSQL-database

This project demonstrates how to transfer data between two PostgreSQL databases using Docker and Python.

1. Set Up PostgreSQL Containers with Docker
-Create two PostgreSQL containers: one for the source database and one for the target database.
-Specify environment variables for each container, including the username, password, and database name.
-Map different ports for each container to avoid conflicts.

2. Verify Containers Are Running
-Use Docker commands to list running containers and ensure both PostgreSQL instances are active.

3. Create Tables and Insert Data
-Access the source database container and create a customers table.
-Insert sample data into the customers table in the source database.
-Access the target database container and create an identical customers table without inserting any data.

4. Data Transfer Using Python
-Write a Python script to connect to both the source and target databases.
-Fetch data from the source database and insert it into the target database.
-Use the psycopg2 library for PostgreSQL connections and data manipulation.

5. Run the Python Script
-Execute the Python script to transfer data from the source database to the target database.
-Verify the data has been successfully transferred.

Conclusion
-This project provides a clear example of how to use Docker and Python for efficient data transfer between PostgreSQL databases. By following these steps, you can easily replicate the process in your own projects.
