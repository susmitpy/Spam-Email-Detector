#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:03:40 2020

@author: susmitvengurlekar
"""

#TODO: Extract Text, Attachment 

import re
import os
from email.parser import HeaderParser
import csv

path_to_spam_header_csv = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_spam_header_text.csv"
path_to_spam_header_body_csv = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_spam_header_body_text.csv"
path_to_spam_header = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Spam/headers/text"

# Regex Patterns
from_pattern = re.compile(r"(From: ?.+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-])",flags=re.IGNORECASE)
sender_email_pattern = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)",flags=re.IGNORECASE)
reply_to_pattern = re.compile(r"Reply-To: .+")
reply_to_email_pattern = re.compile(r"<.+>")
subject_line_pattern = re.compile(r"Subject: .+")
inline_image_pattern = re.compile(r"img +src",flags=re.IGNORECASE)

field_names = ["sender_email","reply_to_email","return_path","inline_image_count","Label"]
csv_file = open(path_to_spam_header_csv,"w")
writer = csv.DictWriter(csv_file,fieldnames=field_names)
writer.writeheader()

body_field_names = ["Subject","Text","Label"]
body_csv_file = open(path_to_spam_header_body_csv,"w")
body_writer = csv.DictWriter(body_csv_file,fieldnames=body_field_names)
body_writer.writeheader()

os.chdir(path_to_spam_header)
row = {"Label":"Spam"}
body_row = {"Label":"Spam"}
parser = HeaderParser()

for file in os.listdir():
    f = open(file,"r",encoding="latin-1")
    txt = f.read()
    f.close()

    try:
        h = parser.parsestr(txt)
        
        from_text = h["From"]
        if from_text == None:
            from_text=""
        try:
            sender_email = re.search(sender_email_pattern,from_text).group()
            row["sender_email"] = sender_email
        except AttributeError as e:
            row["sender_email"] = ""
    
        reply_to_text = h["Reply-To"]
        if reply_to_text == None:
            reply_to_text = ""
        try:
            reply_to_text = re.search(sender_email_pattern,reply_to_text).group()
            row["reply_to_email"] = reply_to_text
        except AttributeError as e:
            row["reply_to_email"] = ""
        
        return_path_text = h["Return-Path"]
        if return_path_text == None:
            return_path_text = ""
        try:
            return_path = re.search(sender_email_pattern,return_path_text).group()
            row["return_path"] = return_path
        except AttributeError as e:
            row["return_path"] = ""

        inline_images = re.findall(inline_image_pattern,txt)
        row["inline_image_count"] = len(inline_images)
        
        writer.writerow(row)
        
      
        
        payload = h.get_payload()
        
        body_row["Subject"] = h["Subject"]
        body_row["Text"] = payload
        body_writer.writerow(body_row)
        
        
    except AttributeError as e:
        print(e)