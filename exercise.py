import pyodbc;

def access_database(database):
        #print('Accessing database...')
        user_login = 'rawson_duplantis1'
        user_pass = 'MIS4322student'

        # The following SQL input is listed in pyodbc documentation, essentially concatenates each line.
        cn_str = (
            'Driver={SQL Server};'
            'Server=MIS-SQLJB;'
            'Database=School;'
            'UID='+user_login+';'
            'PWD='+user_pass+';'
        )

        cn = pyodbc.connect(cn_str) # Enter SQL and connect to database
        cursor = cn.cursor() # A cursor creates a space in local memory to dump records from the SQL server
        cursor.execute(f'select * from School.dbo.{database}') #{database}.{schema}.{table}
        data = cursor.fetchall()
        return data

# ** 1) Calculate the new budget for each department. Every department will be getting a 10% increase in their budget except for the Information Systems (IS) and Computer Science (CS) departments. The IS department gets a 20% increase and the CS department gets a 15 % increase. Create a well formatted report that shows each department name, their current budget, their new budget and the amount increased.
'''
Dept Name				Original Budget		New Budget		Increse in Budget
Engineering				$350,000.00			$385,000.00		$35,000.00
English					$120,000.00			$132,000.00		$12,000.00
Economics				$200,000.00			$220,000.00		$20,000.00
Mathematics				$250,000.00			$275,000.00		$25,000.00
Information Systems		$375,000.00			$450,000.00		$75,000.00
Computer Science		$310,500.00			$357,075.00		$46,575.00                                                     
'''

table_dept = 'Department'
data_dept = access_database(table_dept)
clean_data = {}
for row in data_dept:
    dept_name = row[1]
    dept_pay_orig = int(row[2])
    if dept_name == 'Computer Science':
        dept_pay_new = dept_pay_orig * 1.15
    elif dept_name == 'Information Systems':
        dept_pay_new = dept_pay_orig * 1.2
    else:
        dept_pay_new = dept_pay_orig * 1.1
    dept_pay_increase = dept_pay_new - dept_pay_orig
    clean_data[dept_name] = [dept_pay_orig, dept_pay_new, dept_pay_increase]

# Print-out
def print_increase(clean_data):
    print(format('Dept. Name', '24'), format('Original Budget', '20'), format('New Budget', '16'), format('Increase in Budget', '24'), sep='')
    for dept in clean_data:
        print(format(dept, '24'), format('$' + f'{clean_data[dept][0]:,.2f}', '<20'), format('$' + f'{clean_data[dept][1]:,.2f}', '16'), format('$' + f'{clean_data[dept][2]:,.2f}', '24'), sep='')

#print_increase(clean_data)


# ** 2) Display First Name, Last Name and corresponding personal and work email for STUDENTS ONLY using Person and Contact_Info tables as shown below (only first row shown):
'''
firstname	lastname	Personal Email					Work Email
Gytis		Barzdukas	josephine_darakjy@darakjy.org	ezekiel@chui.com
Peggy		Justice		art@venere.org					wkusko@yahoo.com
Yan			Li			lpaprocki@hotmail.com			bfigeroa@aol.com
Laura		Norman		donette.foller@cox.net			ammie@corrio.com
Nino		Olivotto	simona@morasca.com				francine_vocelka@vocelka.com
'''

table_contacts = 'Contact_Info'
table_person = 'Person'
data_contacts = access_database(table_contacts)
data_person = access_database(table_person)

# Filter students dict from Person table to only include students
students = {}
for person in data_person:
    if person[4]:
        # students[person_id] = [last_name, first_name, email_personal, email_work]
        students[person[0]] = [person[1], person[2], None, None]

# Iterate through each contact and assign to array position within matching student depending on email type
for contact in data_contacts:
    if int(contact[0]) in list(students.keys()):
        email_type = contact[4]
        if email_type == 'Personal':
            students[int(contact[0])][2] = contact[5]
        elif email_type == 'Work':
            students[int(contact[0])][3] = contact[5]

def print_students(students):
    print(format('First', '12'), format('Last', '12'), format('Personal Email', '32'), format('Work Email', '32'), sep='')
    for stu_id in list(students.keys()):
        print(format(students[stu_id][1], '12'), format(students[stu_id][0], '12'), format(students[stu_id][2], '32'), format(students[stu_id][3], '32'), sep='')

#print_students(students)

# ** 3) Display First Name, Last Name and corresponding home,cell and work phone numbers for instructors only using Person and Contact_Info tables as shown below (only first 2 rows shown):
'''
FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone
Kim			Abercrombie		(504) 621-8927	(410) 621-8927	(313) 621-8927
Fadi		Fakhouri		(810) 292-9388	(215) 292-9388	(815) 292-9388
'''

table_contacts = 'Contact_Info'
table_person = 'Person'
data_contacts = access_database(table_contacts)
data_person = access_database(table_person)

# Filter instructors dict from Person table to only include instructors
instructors = {}
for person in data_person:
    if person[3]:
        # instructors[person_id] = [last_name, first_name, phone_home, phone_cell, phone_work]
        instructors[person[0]] = [person[1], person[2], None, None, None]

# Iterate through each contact and assign to array position within matching instructor depending on phone type
for contact in data_contacts:
    if int(contact[0]) in list(instructors.keys()):
        phone_type = contact[1]
        phone_area_code = contact[2]
        if phone_type == 'home':
            instructors[int(contact[0])][2] = f'({contact[2]}) ' + contact[3]
        elif phone_type == 'cell':
            instructors[int(contact[0])][3] = f'({contact[2]}) ' + contact[3]
        elif phone_type == 'work':
            instructors[int(contact[0])][4] = f'({contact[2]}) ' + contact[3]

def print_instructors(instructors):
    print(format('First', '12'), format('Last', '16'), format('Home Phone', '16'), format('Cell Phone', '16'), format('Work Phone', '16'), sep='')
    for instructor_id in list(instructors.keys()):
        print(format(instructors[instructor_id][1], '12'), format(instructors[instructor_id][0], '16'), format(instructors[instructor_id][2], '16'), format(instructors[instructor_id][3], '16'), format(instructors[instructor_id][4], '16'), sep='')

#print_instructors(instructors)