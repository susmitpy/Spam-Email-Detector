#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:28:16 2020

@author: susmitvengurlekar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:21:48 2020

@author: susmitvengurlekar
"""

from email.parser import HeaderParser
import os
import re
import csv

sender_mail_pattern = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)",flags=re.IGNORECASE)
inline_image_pattern = re.compile(r"img +src",flags=re.IGNORECASE)

path_to_email_headers = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Spam/headers/email/"
path_to_header_csv_file = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_spam_header.csv"
path_to_body_csv_file = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_spam_body.csv"

parser = HeaderParser()


header_row = {"sender_email":"","reply_to_email":"","subject":"","inline_image_count":"","Label":"Spam"}
body_row = {"Subject":"","Text":"","Label":"Spam"}

header_field_names = ["sender_email","reply_to_email","subject","inline_image_count","Label"]
header_csv_file = open(path_to_header_csv_file,"w")
header_writer = csv.DictWriter(header_csv_file,fieldnames=header_field_names)
header_writer.writeheader()

body_field_names = ["Subject","Text","Label"]
body_csv_file = open(path_to_body_csv_file,"w")
body_writer = csv.DictWriter(body_csv_file,fieldnames=body_field_names)
body_writer.writeheader()


a = os.listdir(path_to_email_headers)
for f in a:
    header_row = {"sender_email":"","reply_to_email":"","subject":"","inline_image_count":"","Label":"Spam"}
    body_row = {"Subject":"","Text":"","Label":"Spam"}
    try:
        mail = open(path_to_email_headers+f,"r")
        h = parser.parsestr(mail.read())
        
        sender_mail = re.search(sender_mail_pattern,h["From"]).group()
        header_row["sender_email"] = sender_mail
        
        return_path = re.search(sender_mail_pattern,h["Return-Path"]).group()
        header_row["reply_to_email"] = return_path
        

        header_row["subject"] = h["Subject"][4:]
        
        body_row["Subject"] = h["Subject"][4:]
        body_row["Text"] = h.get_payload()
        
        inline_images = re.findall(inline_image_pattern,h.get_payload())
        num_inline_images = len(inline_images)
        
        header_row["inline_image_count"] = num_inline_images
        
        
        header_writer.writerow(header_row)
        print("Header Written")
        body_writer.writerow(body_row)
        
        print("Written")
        
        
    except Exception as e:
        print(e)
