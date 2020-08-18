import pandas as pd
import numpy as np
import re

from nltk.corpus import words
import nltk


first_names = pd.read_csv("./first_names.csv")
words = {i.lower() for i in words.words()}

actual_words = words.union(set(first_names))

df = pd.read_csv("../Raw Data/extracted_header.csv")

df["has_inline_image"] = df["inline_image_count"] >= 1
df.drop(["inline_image_count"],axis=1,inplace=True)

df["no_reply_to_email"] = df["reply_to_email"].isna() # true -> does not have
df["no_return_path"] = df["return_path"].isna() # true -> does not have

df["no_reply_no_return"] = (df["no_reply_to_email"] == True) & (df["no_return_path"] == True)
df["yes_reply_no_return"] = (df["no_reply_to_email"] == False) & (df["no_return_path"] == True)

df.drop(["reply_to_email","return_path","no_reply_to_email"],axis=1,inplace=True)

df = df.dropna()

domain_pattern_compiled = re.compile(r"(@.+)(\.\w+)")
def get_domain(email):
    return domain_pattern_compiled.search(email).groups()[0][1:]
    
df["domain"] = df["sender_email"].apply(get_domain)

account_pattern_compiled = re.compile(r"(.+@)")
def get_account(email):
    return account_pattern_compiled.search(email).groups()[0][:-1]
    
df["account_name"] = df["sender_email"].apply(get_account)

df["free_in_domain"] = df["domain"].map(lambda x: "free" in x)

df.drop(["sender_email","domain"],axis=1,inplace=True)

def is_actual_word(x,first_n_chars=3):
    if len(x) < first_n_chars:
        return False
    
    word_part = x[:first_n_chars]
    if word_part in actual_words:
        return True
    
    return is_actual_word(x,first_n_chars=first_n_chars+1)

df["real_word_in_account"] = df["account_name"].map(is_actual_word)

df = df[["real_word_in_account","has_inline_image","no_return_path","no_reply_no_return","yes_reply_no_return","free_in_domain","Label"]]

df.to_csv("../Processed Data/header.csv",index=False)