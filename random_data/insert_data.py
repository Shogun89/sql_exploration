# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:00:02 2020

@author: ryhow
"""

import pandas as pd
import mysql.connector
import os
import random
from os.path import isfile, join

def insert_purchases(cursor, cnx):
    
    path = os.getcwd()

    mypath= os.path.join(path, 'purchase_data')
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    i = 1
    for file in onlyfiles:
        
   
        filepath = join(mypath, file)
        filepath = filepath.replace("\\", "/")
        print("Inserting into purchases - File # : ", i)
        q = """
        LOAD DATA INFILE '{file}' 
        INTO TABLE purchases
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (product_id, invoice_id)""".format(file = filepath)
        
        cursor.execute(q)
        cnx.commit()
        i+=1


        
def insert_invoices( cursor, cnx):
 
    print('Inserting into invoices')    
    q =  """ 
    LOAD DATA INFILE 'D:/Users/ryhow/Documents/Python/random_purchases/invoice_sample.csv' 
    INTO TABLE invoices 
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (purchase_start, purchase_end, store_id)"""
    cursor.execute(q)
    cnx.commit()
    
def insert_stores(cursor, cnx):
    
    def make_stores():
        stores = list(range(1,52))
        location_ids = [random.randint(1,51) for i in stores]
        
        data = {'location_id': location_ids}
        df = pd.DataFrame(data)
        
        
        return df
    df = make_stores()
    print('Inserting in stores')
    records = list(df.itertuples(index=False, name=None))
    q = """ 
    INSERT INTO stores (location_id) 
    VALUES (%s)"""
    cursor.executemany(q,records)
    cnx.commit()


def main():
    
    #### MySQL connection
    creds = os.environ['MYSQL_TEST'].split('@#$')
    cnx = mysql.connector.connect(host=creds[0],user=creds[1],password=creds[2],database=creds[3])
    cursor = cnx.cursor()
    
    insert_stores(cursor,cnx)
    insert_invoices(cursor, cnx)
    insert_purchases(cursor, cnx)
    
if __name__ == "__main__":
    main()