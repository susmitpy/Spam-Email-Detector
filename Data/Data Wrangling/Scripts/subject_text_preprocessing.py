import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords

df = pd.read_csv("../Raw Data/extracted_body.csv")

df["no_subject"] = df["Subject"].isna()
df["no_text"] = df["Text"].isna()

df["Subject"] = df["Subject"].fillna("")
df["Text"] = df["Text"].fillna("")

df["is_html"] = df["Text"].map(lambda x: "<html" in str(x).lower() or "< html" in str(x).lower())
df["http_count"] = df["Text"].str.count("http")

url_pattern = re.compile(r"(https?://[\w\.]+)",re.IGNORECASE)
def url_count_in_text(text):
    url_free_text = re.sub(url_pattern,"",text)
    return url_free_text
df["Text"] = df["Text"].map(url_count_in_text)

df["Text"] = df["Text"].str.lower().str.findall(r"[a-z]+")

remove_words = set(stopwords.words())
tags = set(["html","head","img","p","div","body","title"])
remove_words = remove_words.union(tags)
def remove_tags(text):
    cleaned_text = []
    for txt in text:
        if txt in remove_words:
            continue
        cleaned_text.append(txt)
    return cleaned_text
df["Text"] = df["Text"].map(remove_tags)

html_removal_phrases = ["this part message mime","this multipart mime message","content type"]
def html_removal(text):
    text = " ".join(text)
    for remove in html_removal_phrases:
        text = text.replace(remove,"")
    text = text.strip()
    text = text.lower()
    return text
df["Text"] = df["Text"].map(html_removal)

remove_phase_two = ["part message mime","multipart message mime","text plain","content transfer","charset","us ascii","format","encoding","multipart","body","html","head","title","meta"]
def phase_two(text):
    for remove in remove_phase_two:
        text = text.replace(remove,"")
    text = text.strip()
    text = text.lower()
    return text
df["Text"] = df["Text"].map(phase_two)

def cleaner(text):
    text = text.split(" ")
    cleaned = []
    for txt in text:
        txt = txt.strip()
        if len(txt) > 2:
            cleaned.append(txt)
    return " ".join(cleaned)
df["Text"] = df["Text"].map(cleaner)

df["Text"] = df["Text"].str.join("")

df["Subject"] = df["Subject"].str.lower().str.findall(r"[a-z]+")

stopwords = set(stopwords.words())
def stop_word_remover(text):
    cleaned = []
    for txt in text:
        txt = txt.strip()
        if len(txt) < 3:
            continue
        if txt in stopwords:
            continue
        cleaned.append(txt)
    return " ".join(cleaned)
df["Subject"] = df["Subject"].map(stop_word_remover)

df.to_csv("../Processed Data/body_processed.csv",index=False)
