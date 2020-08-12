#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:31:06 2020

@author: susmitvengurlekar
"""

import os

path = "/Users/susmitvengurlekar/Downloads/lingspam_public/lemm_stop/"
path_to_body_folder = "/Users/susmitvengurlekar/Downloads/Spam/body/"
path_to_ham_body_folder = "/Users/susmitvengurlekar/Downloads/Ham/body/"
os.chdir(path)
for part in os.listdir():
    if part != ".DS_Store":
        os.chdir(path + f"{part}/")
        files = os.listdir()
        for file in files:
            if file.startswith("spmsg"):
                # Put in spam body
                os.system(f"mv {os.getcwd()}/{file} {path_to_body_folder}")
            else:
                os.system(f"mv {os.getcwd()}/{file} {path_to_ham_body_folder}")
    
        