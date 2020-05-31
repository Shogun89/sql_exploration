# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:19:00 2020

@author: ryhow
"""

import os
import mysql.connector
from mysql.connector import errorcode


def main():
    

    TABLES = {}
    TABLES['products'] = (
        """ 
        CREATE TABLE products (
          id int(11) NOT NULL AUTO_INCREMENT,
          product_name VARCHAR(26) NOT NULL,
          product_type VARCHAR(26) NOT NULL,
          cost  DECIMAL(15,2) NOT NULL, 
          PRIMARY KEY (id) );""")
    
    
    
    TABLES['locations'] = (
        """ CREATE TABLE locations (
          id int(11) NOT NULL AUTO_INCREMENT,
          state_name VARCHAR(30),
          state_code CHAR(2),
          PRIMARY KEY (id) ); """ )
    
    
    TABLES['stores'] = (
        """ CREATE TABLE stores (
          id int(11) NOT NULL AUTO_INCREMENT,
          location_id int(3) NOT NULL,
          PRIMARY KEY (id) ,
          FOREIGN KEY (location_id) REFERENCES locations(id)); """)
        
    TABLES['invoices'] = (
        """ CREATE TABLE invoices (
          id int(11) NOT NULL AUTO_INCREMENT,
          purchase_start DATETIME NOT NULL,
          purchase_end DATETIME NOT NULL,
          store_id INT(11) NOT NULL,
          PRIMARY KEY (id) ,
          FOREIGN KEY (store_id) REFERENCES stores(id) );""" )
    
    TABLES['purchases'] = (
        """ 
        CREATE TABLE purchases (
          id int(11) NOT NULL AUTO_INCREMENT,
          product_id INT(11) NOT NULL,
          invoice_id INT(11) NOT NULL,
          PRIMARY KEY (id)  ,
          FOREIGN KEY (product_id) REFERENCES products(id) );""" )
   
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
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
