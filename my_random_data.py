# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:06:35 2020

@author: ryhow
"""

from random_data import drop_schemas, drop_tables, generate_schemas, generate_tables
from random_data import  insert_basic_data, insert_data,generate_data, generate_agg_tables
## from random_data.initialize import drop_tables, generate_schemas, generate_tables
### from random_data.data_gen import generate_data, insert_basic_data, insert_data
### from random_data.data_agg import generate_agg_tables, insert_agg_data
##

def main():
    
    ### Drop stuff ###
    #drop_schemas.main()
    drop_tables.main()
    ### Generate schemas 
    generate_schemas.main()
    ### Generates invoices and purchases
    generate_data.main()
    ### Construct tables
    generate_tables.main()
    ### Inserts basic data
    insert_basic_data.main()
    ### Insert data
    insert_data.main()
    
    ## Generate aggregate tables
    #generate_agg_tables.main()
    
    ### Insert agg table data
    # insert_agg_data.main()
    
    
if __name__ == "__main__":
    main()