import pandas as pd
import numpy as np
import csv

# from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("IMDB Dataset.csv")

# print(df.iloc[0:2,])
# print(df.info())

# print(df['review'].head())
df['new_review'] = df['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))

df['new_review'] = df['new_review'].str.replace('[^\w\s]','')

df['new_review'] = df['new_review'].str.replace('br','')

# print(df['new_df'].head())

print(df['new_review'].head(5))

