#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:03:40 2020

@author: susmitvengurlekar
"""

#TODO: Extract Text, Attachment 

import re
import os

import csv

path_to_spam_header_csv = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/csvs/extracted_spam_header_text.csv"
path_to_spam_header = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Spam/headers/text"

# Regex Patterns
from_pattern = re.compile(r"(From: ?.+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-])",flags=re.IGNORECASE)
sender_email_pattern = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)",flags=re.IGNORECASE)
reply_to_pattern = re.compile(r"Reply-To: .+")
reply_to_email_pattern = re.compile(r"<.+>")
subject_line_pattern = re.compile(r"Subject: .+")
inline_image_pattern = re.compile(r"img +src",flags=re.IGNORECASE)

field_names = ["sender_email","reply_to_email","subject","inline_image_count","Label"]
csv_file = open(path_to_spam_header_csv,"w")
writer = csv.DictWriter(csv_file,fieldnames=field_names)
writer.writeheader()

os.chdir(path_to_spam_header)
row = {"Label":"Spam"}

for file in os.listdir():
    f = open(file,"r",encoding="latin-1")
    txt = f.read()
    f.close()

    try:
        from_text = re.search(from_pattern,txt).group()
        sender_email = re.search(sender_email_pattern,from_text).group()
        row["sender_email"] = sender_email
    
        try:
            reply_to_text = re.search(reply_to_pattern,txt).group()
        
            reply_to_email = re.search(reply_to_email_pattern,reply_to_text).group()[1:-1]
            row["reply_to_email"] = reply_to_email
        except AttributeError:
            row["reply_to_email"] = "None"
        
        
        subject_line = re.search(subject_line_pattern,txt).group()
        subject_text = subject_line[9:]
        row["subject"] = subject_text
        
        
        inline_images = re.findall(inline_image_pattern,txt)
        row["inline_image_count"] = len(inline_images)
        
        writer.writerow(row)
    except AttributeError:
        continue