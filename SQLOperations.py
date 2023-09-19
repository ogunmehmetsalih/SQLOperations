import pypyodbc

class MSSQLDatabase:
    def __init__(self,server,database):
        self.server=server
        self.database=database

    def __enter__(self):
        self.conn = pypyodbc.connect(
            f"Driver={{SQL Server}};"
            f"Server={self.server};"
            f"Database={self.database};"
            "Trusted_Connection=True"
        )

        return self
    def __exit__(self, exc_type, exc_val, exc_traceb):
        self.conn.close()

    def execute_query(self,sql,params=None):
        cursor=self.conn.cursor()
        if params:
            cursor.execute(sql,params)
        else:
            cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def create_table(self,table_name,columns):
        sql=f"CREATE TABLE {table_name} ({columns})"
        self.execute_query(sql)

    def drop_table(self,table_name):
        sql=f"DROP TABLE {table_name}"

    def insert_data(self,table_name,values):
        sql=f"INSERT INTO {table_name} VALUES {values}"
        self.execute_query(sql)

    def delete_data(self,table_name,condition):
        sql=f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(sql)

    def create_database(self):
        pass
        """database oluşturma,silme işleminde hata aldım"""
    def drop_database(self):
        pass

    def show_data(self,table_name):
        sql=f"SELECT * FROM {table_name}"
        cursor=self.conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            print(row)








