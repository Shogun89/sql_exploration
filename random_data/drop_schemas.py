# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:04:17 2020

@author: ryhow
"""
import os
import mysql.connector
from mysql.connector import errorcode


def main():
    

    SCHEMAS = {}
    
    SCHEMAS['test_data'] = (
        """ 
        DROP SCHEMA test_data ;""")
    
    SCHEMAS['dw_tables'] = (
            """ DROP SCHEMA dw_tables;""")
    
    
    
    
        
    
   
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    for schema_name in SCHEMAS:
        schema_description = SCHEMAS[schema_name]
        try:
            print("Dropping schema {}: ".format(schema_name), end='')
            cursor.execute(schema_description)
        except mysql.connector.Error as err:
            if err.errno ==  errorcode.ER_SCHEMA_EXISTS_ERROR:
                print("Doesn't exist.")
            else:
                print(err.msg)
        else:
            print("OK")
    
    cursor.close()
    cnx.close()
    


if __name__ == "__main__":
    main()