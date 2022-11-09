# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:18:24 2022

@author: Sabari
"""

import pymongo

mongo=pymongo.MongoClient("mongodb://127.0.0.1:27017")

db=mongo["telephone_dir"]

coll=db["dir"]

dir_details=[ { "Name":"sabari","Phone":9877721334,"Email":"sabari@gmail.com","Place":{"Country":"India","State":"TamilNadu" } },
              { "Name":"Nathan","Phone":9873214521,"Email":"sabari213@gmail.com","Place":{"Country":"India","State":"Telungana" } },
              { "Name":"Nathan","Phone":9873214521,"Email":"sabari213@gmail.com","Place":{"Country":"India","State":"Telungana" } }]

data=coll.insert_many(dir_details)             

find_data = coll.find()           

for elem in find_data:
    print(elem)

#------------ update_one--------------------------

myquery = { "Email":"sabari213@gmail.com"} 

new_query = { "$set" : {"Phone":7072308314}}

update_query = coll.update_one(myquery,new_query)   

find_data1 = coll.find()

print(" ************ After Update ************ ")
for elem1 in find_data1:
    print(elem1)

#-------------- delete_one ---------------------

del_query= { "Email":"sabari213@gmail.com" }

coll.delete_one( del_query )
find_data2 = coll.find()

print(" ************ After Delete ************ ")
for elem2 in find_data2:
    print(elem2)
    
    
    