import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

df = pd.read_csv("../Processed Data/body_processed.csv",keep_default_na=False)

def stem_text(tokens):
    ps = PorterStemmer()
    combined = []
    for token in tokens:
        combined.append(ps.stem(token))
    return " ".join(combined)

df["Text"] = df["Text"].map(lambda x: word_tokenize(x))
df["Subject"] = df["Subject"].map(lambda x: word_tokenize(x))

df["Text"] = df["Text"].map(stem_text)
df["Subject"] = df["Subject"].map(stem_text)

nlp_data = df[["Subject","Text","Label"]]
nlp_data = nlp_data.dropna()

df = df.drop(["Subject","Text"],axis=1)

nlp_data.to_csv("../../Modelling/Data/nlp_data.csv",index=False)
df.to_csv("../../Modelling/Data/body_features.csv",index=False)