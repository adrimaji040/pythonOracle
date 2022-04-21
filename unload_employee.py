import cx_Oracle
import config
import json

list_employees = []
sql_str = "select employee_id, first_name, last_name,to_char(hire_date,'yyyy-mm-dd') hire_date, job_title from employees where rownum < 10"

try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dns,
            encoding=config.encoding) as conn:
            
        # create cursor object
        cur = conn.cursor()

        # query to get  all the data
        cur.execute(sql_str) 

        # print each row in the cursor
        for employee_id, first_name, last_name, hire_date, job_title in cur:
            list_employees.append({ 'employee_id' : employee_id, 'first_name:' : first_name, 'last_name' : last_name,
                                    'hire_date' : hire_date, 'job_title' : job_title})
except cx_Oracle.Error as er:
    print(er)

for y  in list_employees:
    print(json.dumps(y, indent = 4, sort_keys = True))

# Write the list of dictionary employees within a jason file 
with open('list_employees.json', 'w') as outfile:
    json.dump(list_employees, outfile, indent = 4, sort_keys = True)

