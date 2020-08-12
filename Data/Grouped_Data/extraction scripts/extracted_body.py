#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:45:17 2020

@author: susmitvengurlekar
"""

import csv
import os

path_to_body_csv = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_body.csv"
path_to_spam_body = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Spam/body"
path_to_ham_body = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Ham/body"

csv_file = open(path_to_body_csv,"w")
writer = csv.DictWriter(csv_file,fieldnames=["Subject","Text","Label"])
writer.writeheader()

os.chdir(path_to_spam_body)
data = {"Subject":"","Text":"","Label":"Spam"}

for file in os.listdir():
    f = open(file)
    lines = f.readlines()
    f.close()
    
    data["Subject"] = lines[0][9:]
    data["Text"] = " ".join(lines[2:])
    
    writer.writerow(data)
    
os.chdir(path_to_ham_body)
data = {"Subject":"","Text":"","Label":"Ham"}

for file in os.listdir():
    f = open(file)
    lines = f.readlines()
    f.close()
    
    data["Subject"] = lines[0][9:]
    data["Text"] = " ".join(lines[2:])
    
    writer.writerow(data)





csv_file.close()
