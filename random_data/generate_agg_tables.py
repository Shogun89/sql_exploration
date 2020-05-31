# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:51:51 2020

@author: ryhow
"""
import os
import mysql.connector
from mysql.connector import errorcode


def generate_tables():
    
    TABLES = {}
    
    for i in list(range(1,53)):
        tbl_name = 'dw_weekly_sales_{num}'.format(num= i)
        
        TABLES[tbl_name] = (
        """ 
        CREATE TABLE {tbl} (
          id int(11) NOT NULL AUTO_INCREMENT,
          store_id INT(11) NOT NULL,
          burger_sales DECIMAL(15,2) NOT NULL,
          fish_sales DECIMAL(15,2) NOT NULL,
          beverage_sales DECIMAL(15,2) NOT NULL,
          nugget_sales DECIMAL(15,2) NOT NULL,
          fry_sales DECIMAL(15,2) NOT NULL,
          dessert_sales DECIMAL(15,2) NOT NULL,
          
          
          PRIMARY KEY (id),
        
          FOREIGN KEY (store_id) REFERENCES test_data.stores(id) );""".format(tbl = tbl_name))
        
    return TABLES
        
  
    
def main():
    
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    TABLES = generate_tables()
    cursor.execute("USE dw_tables")
    
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
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

    