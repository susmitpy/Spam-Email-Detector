#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:15:16 2020

@author: susmitvengurlekar

Group files in different folders of eron data set under a folder which contains headers
"""

import os

path = "/Users/susmitvengurlekar/Email/Data/Raw_Data/BG (Spam)/"
path_to_header_folder = "/Users/susmitvengurlekar/Email/Data/Grouped_Data/Spam/headers/text"
os.chdir(path)
for year in os.listdir():
    if year != ".DS_Store":
        os.chdir(path + f"{year}/")
        for month in os.listdir():
            if month != ".DS_Store":
                os.chdir(path + f"{year}/" + f"{month}/")
                os.system(f"mv *.txt {path_to_header_folder}")
