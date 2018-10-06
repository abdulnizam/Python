#!/usr/bin/env python

import os


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import mysql.connector
import json

mydb = mysql.connector.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USERNAME'),
  passwd=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)

json = {
	"data":
	[
		{
			"transactions_id": "001538148155615",
			"COUNT(transactions_id)": 2,
			"created_at": "2018-09-28 19:22:34"
		},
		{
			"transactions_id": "011538066236557",
			"COUNT(transactions_id)": 2,
			"created_at": "2018-09-27 20:37:15"
		},
		{
			"transactions_id": "011538225813940",
			"COUNT(transactions_id)": 2,
			"created_at": "2018-09-29 16:56:53"
		}
	]
};

leng = len(json['data'])

mycursor = mydb.cursor()

# xrange can be used in python 2 and it deprecated in python 3

for x in range(leng):
	
	sql = "DELETE t1 FROM transactions t1 INNER JOIN transactions t2 WHERE t1.id < t2.id AND t1.transactions_id = t2.transactions_id AND t1.transactions_id = '" + json['data'][x]['transactions_id'] + "'";

	mycursor.execute(sql)

	mydb.commit()

	print(mycursor.rowcount, "record(s) deleted")
