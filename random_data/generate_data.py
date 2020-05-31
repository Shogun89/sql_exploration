# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:43:24 2020

@author: ryhow
"""

import pandas as pd
import random 
import os
from numpy.random import choice

def make_invoice_data():
    start_date = '2019-01-01' 
    end_date = '2019-12-31'
 
    invoice_data = pd.DataFrame(pd.date_range(start=start_date, end = end_date ,freq="2min"), columns=['start_date'])
    invoice_data['end_date'] = invoice_data['start_date'].apply(lambda x: x + random.randint(1,10) * pd.DateOffset(minutes=1))
    
    invoice_data['start_date'] = pd.to_datetime(invoice_data['start_date'], format='%Y-%m-%d %H:%M:%S')
    invoice_data['end_date']  = pd.to_datetime(invoice_data['end_date'], format='%Y-%m-%d %H:%M:%S')
    return invoice_data

def generate_invoice_sample(store_num, invoice_data):
    
    sample_size = random.randint(100,300)*365
    sample = invoice_data.sample(sample_size)
    sample['store_id'] = store_num
    
    return sample

def generate_purchase(invoices):
    ### Generate a list of purchase for a given invoice (generates random product ids)

    n = 100000
    
    purchases = [random.choice(invoices) for i in range(n)]
    weights = [.19]+ [.08]*10 + [.01] 
    product_choices = list(range(1,13))
    
    products = choice(product_choices, n,
              p=weights)

    
    data = {'product_id': products, 'invoice_id' : purchases}
    df = pd.DataFrame(data)
    return df

def main():
    
    main_invoices = make_invoice_data()

    ### This is arbitrary (originally intended it to be much larger but it's time consuming)
    stores = list(range(1,51))
    
    invoice_data = []
    
    for store in stores:
        print('Invoice #' , store)
        sample = generate_invoice_sample(store, main_invoices)
        invoice_data.append(sample)
        
    
    ### Makes invoices
    invoice_result = pd.concat(invoice_data)
    #n = 2500000
    num_rows = range(len(invoice_result))
    invoice_result.to_csv("invoice_sample.csv", index=False)
    
    chunk_size = 50000
    purchase_chunks = [num_rows[i:i + chunk_size] for i in range(0, len(num_rows), chunk_size)]
    i = 1
    path = os.getcwd()
    
    for chunk in purchase_chunks:
        print('Purchase Chunk ', i)
        data = generate_purchase(chunk)
        filename = 'purchase_data\\purchase_{num}.csv'.format(num=i)

        data_name = os.path.join(path, filename)
        data.to_csv(data_name, index=False)
        i+=1
    
    ### Makes the store data
    locations = [random.randint(1,51) for i in stores]
    data  = {'id': stores, 'store_id':locations}
    store_result = pd.DataFrame(data)

    store_result.to_csv("store_locations.csv", index=False)
if __name__ == "__main__":
    main()



    
