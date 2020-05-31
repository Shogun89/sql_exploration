# Basic SQL Exploration
This repository is mostly meant to document a small project to understand how to generate random data, do basic SQL queries 
and aggregate larger tables into better more easy to access tables


# About
The project simulates a ficitonal burger chain by giving a basic data model about this chains. There are a few tables that make this happen. They are : invoices, purchases, locations, stores, and products. The basic relationship between them is as follows

* Purchases map to invoices and products. A single invoice could have multiple purchases with it.
* Invoices map to stores which are located in place (here it is the US). Invoices have purchase_start and purchase_end dates.
* Stores map to locations which are simply states in the US.
* Products are what the purchases are made of and can be split into product_types. Each product has a cost and name (product_name).

