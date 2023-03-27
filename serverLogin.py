import tkinter
import pyodbc

class myGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.geometry('200x120')
        self.main.title('SQL Server Login')

        self.frame = tkinter.Frame(self.main, pady=15)
        self.label_login = tkinter.Label(self.frame, text='Login:')
        self.label_pass = tkinter.Label(self.frame, text='Password:')
        self.entry_login = tkinter.Entry(self.frame, width=20)
        self.entry_pass = tkinter.Entry(self.frame, show='*', width=20)
        self.login_button = tkinter.Button(self.main, text='Login', command=self.access_database)

        self.frame.pack()
        self.label_login.grid(row=0, column=0)
        self.label_pass.grid(row=1, column=0)
        self.entry_login.grid(row=0, column=1)
        self.entry_pass.grid(row=1, column=1)
        self.login_button.pack()

        tkinter.mainloop()

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

        for row in data:
            course_ID = row[0]
            course_name = row[1]
            course_credit = row[2]
            course_dept = row[3]
            course_list[course_ID] = [course_name, course_credit, course_dept]
        
        #print(course_list)
        course_id_search = int(input('Course ID to search: '))
        for id, course_info in course_list.items():
            #print(f"{id}, {course_info}")
            if id == course_id_search:
                print(course_list[id])

window = myGUI()