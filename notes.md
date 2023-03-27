### Python + SQL
Connect to the database
```Python
def access_database(self):
        print('Accessing database...')
        #user_login = self.entry_login.get()
        #user_pass = self.entry_pass.get()
        user_login = 'rawson_duplantis1'
        user_pass = 'MIS4322student'
        self.main.destroy()
        #print(f"User: {user_login} Password: {user_pass}")
        # User: rawson_duplantis1
        # MIS4322student

        pre_list = {}
        course_list = {}
        # The following SQL input is listed in pyodbc documentation, essentially concatenates each line.
        cn_str = (
            'Driver={SQL Server};'
            'Server=MIS-SQLJB;'
            'Database=School;'
            'UID='+user_login+';'
            'PWD='+user_pass+';'
        )
        
        cn = pyodbc.connect(cn_str)
        cursor = cn.cursor() # A cursor creates a space in local memory to dump records from the SQL server
        cursor.execute('select * from School.dbo.Course') #{database}.{schema}.{table}
        
        data = cursor.fetchall()
        print(data)
```