import pandas as pd

# Header
spam_header_text = pd.read_csv("./csvs/extracted_spam_header_text.csv")
ham_header = pd.read_csv("./csvs/extracted_ham_header.csv")
spam_header = pd.read_csv("./csvs/extracted_spam_header.csv")
header=pd.concat([ham_header,spam_header,spam_header_text],axis=0).sample(frac=1)
header.to_csv("./merged_csvs/header.csv",index=False)


# Body
spam_header_body_text = pd.read_csv("./csvs/extracted_spam_header_body_text.csv")
spam_body = pd.read_csv("./csvs/extracted_spam_body.csv")
ham_body = pd.read_csv("./csvs/extracted_ham_body.csv")
body = pd.read_csv("./csvs/extracted_body.csv")
final_body = pd.concat([spam_header_body_text,spam_body,ham_body,body],axis=0).sample(frac=1)
final_body.to_csv("./merged_csvs/body.csv",index=False)

