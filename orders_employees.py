#-------------------------------------------------
# Create a file with the orders for each employee
# Created by: Adriana Jimenez
# Start: April 21 -2022
# Inviroment: Oracle Databases, python and json
#------------------------------------------------

import cx_Oracle
import config
import json

list_ordes = []

try:
    with cx_oracle.connect(
            config.username,
            config,password,
            config.dns,
            encoding=config.encoding) as conn:
       
        with conn.cursor() as cur:
            #create new varaibles to hold the value of OUT parameter
            vemployee_id = cur.var(init)
            vorder_id    = cur.var(init)
            vstatus      = cur.var(init)
            
            #call Oracle procedure
            cur.callproc('employee_orders', [vemployee_id, vorder_id, vstatus])



            return vemployee_id.getvalue(), vorder_id.getvalue(), vstatus.getvalue()

except cx_oracle.Error as err:
    print(err)
