# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:18:37 2020

@author: ryhow
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:04:17 2020

@author: ryhow
"""
import os
import mysql.connector
from mysql.connector import errorcode


def main():
    

    TABLES = {}
    
    TABLES['purchases'] = (
        """ 
        DROP TABLE purchases ;""")
    
    TABLES['invoices'] = (
        """ DROP TABLE invoices ; """ )
    
    TABLES['stores'] = (
        """ DROP TABLE stores; """)
    
    TABLES['locations'] = (
        """ DROP TABLES locations ; """ )
    
    
    TABLES['products'] = (
        """ 
        DROP TABLES products ;""")
    
    
    
    
    
    
        
    
   
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Dropping table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno ==  errorcode.ER_TABLE_EXISTS_ERROR:
                print("Doesn't exist.")
            else:
                print(err.msg)
        else:
            print("OK")
    
    cursor.close()
    cnx.close()
    


if __name__ == "__main__":
    main()