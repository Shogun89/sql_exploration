# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:49:08 2020

@author: ryhow
"""

import os
import mysql.connector
from mysql.connector import errorcode

def main():
    TABLES = {}

    #### Generate the products table
    TABLES['products']  = ("""
    
    INSERT INTO products (product_name, product_type, cost)
    VALUES
    	('Big Burger', 'Burger', 5),
        ('Small Burger', 'Burger',3),
        ('Mega Burger', 'Burger', 8),
        ('Fish Filet', 'Fish', 4),
        ('Shake', 'Beverage', 2),
        ('Chicken Nuggets -- 20', 'Nuggets', 8),
        ('Large Fry', 'Fries', 3),
        ('Small Fry', 'Fries', 2),
        ('Soft Drink', 'Beverage', 1),
        ('Coffee', 'Beverage', 1),
        ('Vanilla Cone', 'Dessert', 2),
        ('Apple Pie', 'Dessert', 2);""")
    
    
    #### Generate the area table
    TABLES['locations'] = ("""
    INSERT INTO locations(state_name,state_code) 
    VALUES
     ('Alabama','AL'),
     ('Alaska','AK'),
     ('Arizona','AZ'),
     ('Arkansas','AR'),
     ('California','CA'),
     ('Colorado','CO'),
     ('Connecticut','CT'),
     ('Delaware','DE'),
     ('District of Columbia','DC'),
     ('Florida','FL'),
     ('Georgia','GA'),
     ('Hawaii','HI'),
     ('Idaho','ID'),
     ('Illinois','IL'),
     ('Indiana','IN'),
     ('Iowa','IA'),
     ('Kansas','KS'),
     ('Kentucky','KY'),
     ('Louisiana','LA'),
     ('Maine','ME'),
     ('Maryland','MD'),
     ('Massachusetts','MA'),
     ('Michigan','MI'),
     ('Minnesota','MN'),
     ('Mississippi','MS'),
     ('Missouri','MO'),
     ('Montana','MT'),
     ('Nebraska','NE'),
     ('Nevada','NV'),
     ('New Hampshire','NH'),
     ('New Jersey','NJ'),
     ('New Mexico','NM'),
     ('New York','NY'),
     ('North Carolina','NC'),
     ('North Dakota','ND'),
     ('Ohio','OH'),
     ('Oklahoma','OK'),
     ('Oregon','OR'),
     ('Pennsylvania','PA'),
     ('Rhode Island','RI'),
     ('South Carolina','SC'),
     ('South Dakota','SD'),
     ('Tennessee','TN'),
     ('Texas','TX'),
     ('Utah','UT'),
     ('Vermont','VT'),
     ('Virginia','VA'),
     ('Washington','WA'),
     ('West Virginia','WV'),
     ('Wisconsin','WI'),
     ('Wyoming','WY');""")
    
    
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Inserting into {}: ".format(table_name), end='')
            cursor.execute(table_description)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno ==  errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()
    

if __name__ == "__main__":
    main()