import psycopg2

class DatabaseUtil:

    def __init__(self, db_config):
        self.db_config = db_config
        try:
            self.connetion = psycopg2.connect(**db_config)
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.connetion = None

    def schema_details(self, schema_name):
        """
        This will generate your:
        schema
        each table 
        each column
        with its data type 
        """
        try:
            schema_info_context = ""

            connection = self.connetion
            cursor = connection.cursor()

            schema_info_context = f"Database Schema : {schema_name}\n"

            tables_list = cursor.execute("SELECT table_name from information_schema.tables where table_schema = %s;", (schema_name,))
            tables_list = cursor.fetchall()

            for table in tables_list:
                table_name = table[0]
                schema_info_context = f"{schema_info_context}\nTable: {table_name}\n"

                # Adding columns & Data types
                cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s;", (table_name,))
                columns_list = cursor.fetchall()

                for column in columns_list:
                    columns_name = column[0]
                    data_type = column[1]
                    schema_info_context = f"{schema_info_context} Column: {columns_name}, Data Type: {data_type}\n"

                # Adding Sample Data
                cursor.execute(f"Select * FROM {schema_name}.{table_name} LIMIT 5;")
                sample_data = cursor.fetchall()
                schema_info_context = f"{schema_info_context} Sample Data:\n"
                for row in sample_data:
                    schema_info_context = f"{schema_info_context} {row}\n"
        except Exception as e:
            print("Error fetching schema details: {e}")
            schema_info_context = f"Error fetching schema details: {e}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                
        return schema_info_context

    def execute_query(self,query):
        try:
            connection = self.connection
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            return str(result)
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if cursor:
                cursor().close()
            if connection:
                connection.close()


obj = DatabaseUtil({
    "host":"localhost",
    "port":5432,
    "user":"postgres",
    "password":"Anshi@2004",
    "dbname":"postgres"
})


result = obj.schema_details("public")

with open("test_schema_details.txt","w") as f:
    f.write(result)