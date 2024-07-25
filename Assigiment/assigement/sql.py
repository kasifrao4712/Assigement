import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kasif",
            database="school"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Function to insert a new student record
def insert_student(connection, first_name, last_name, age, grade):
    try:
        cursor = connection.cursor()

        # SQL query to insert a new student record
        sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, age, grade)
        cursor.execute(sql, values)

        # Commit changes to the database
        connection.commit()

        print("Student record inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting student record: {err}")
    finally:
        cursor.close()

# Function to update grade of a student
def update_grade(connection, first_name, new_grade):
    try:
        cursor = connection.cursor()

        # SQL query to update grade of the student
        sql = "UPDATE students SET grade = %s WHERE first_name = %s"
        values = (new_grade, first_name)
        cursor.execute(sql, values)

        # Commit changes to the database
        connection.commit()

        print(f"Grade updated successfully for student {first_name}.")
    except mysql.connector.Error as err:
        print(f"Error updating grade: {err}")
    finally:
        cursor.close()

# Function to delete a student record
def delete_student(connection, last_name):
    try:
        cursor = connection.cursor()

        # SQL query to delete the student record
        sql = "DELETE FROM students WHERE last_name = %s"
        value = (last_name,)
        cursor.execute(sql, value)

        # Commit changes to the database
        connection.commit()

        print(f"Student record with last name {last_name} deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error deleting student record: {err}")
    finally:
        cursor.close()

# Function to fetch and display all student records
def fetch_all_students(connection):
    try:
        cursor = connection.cursor()

        # SQL query to fetch all student records
        sql = "SELECT * FROM students"
        cursor.execute(sql)

        # Fetch all rows
        students = cursor.fetchall()

        # Display fetched records
        if students:
            print("All student records:")
            for student in students:
                print(student)
        else:
            print("No student records found.")
    except mysql.connector.Error as err:
        print(f"Error fetching student records: {err}")
    finally:
        cursor.close()

def main():
    # Connect to MySQL database
    connection = connect_to_mysql()

    if connection:
        # Insert a new student record
        insert_student(connection, "kasif", "Smith", 18, 95.5)

        # Update grade of the student with first name "Alice"
        update_grade(connection, "kasif", 98.7)

        # Delete the student with last name "Smith"
        # delete_student(connection, "Smith")

        # Fetch and display all student records
        fetch_all_students(connection)

        # Close the connection
        connection.close()
    else:
        print("Connection to MySQL failed. Exiting...")

if __name__ == "__main__":
    main()
