# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:50:02 2020

@author: ryhow
"""

import os
import mysql.connector
from mysql.connector import errorcode


def main():
    

    SCHEMAS= {}
    
    SCHEMAS['test_data'] = (
        """ 
        CREATE SCHEMA test_data;""")
    
    SCHEMAS['dw_tables'] = (
        """ 
        CREATE SCHEMA dw_tables;""")
    
   
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    for table_name in SCHEMAS:
        table_description = SCHEMAS[table_name]
        try:
            print("Creating schema {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno ==  errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    
    cursor.close()
    cnx.close()


if __name__ == "__main__":
    main()
