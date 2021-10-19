from numpy.lib.utils import info
import pandas as pd
import numpy as np
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv("IMDB Dataset.csv")

# print(df.iloc[0:2,])
# print(df.info())

# print(df['review'].head())
# df['new_review'] = df['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# # df['new_review'] = df['new_review'].str.replace('[^\w\s]','')

# df['new_review'] = df['new_review'].str.replace("<br />",'')

# print(df['new_review'].head(5))

# print(df['new_review'][0])

# # reviews_str = df['review'].astype(str)
# print(df.dtypes)

# print(df['review'][0])

# print(df['sentiment'== 'positive'])

# def get_feature(x):

#     # Create CountVectorizer, which create bag-of-words model.
#     # stop_words : Specify language to remove stopwords. 

#     # Learn vocabulary in sentences. 
#     vectorizer.fit(x)

#     # Get dictionary. 
#     # print(len(vectorizer.get_feature_names()))
#     print(vectorizer.get_feature_names())
    

# vectorizer = CountVectorizer(stop_words='english')

df_pos = df[df['sentiment'] == "positive"]

df_neg = df[df['sentiment'] == "negative"]

pos_cnt = df_pos.review.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)

neg_cnt = df_neg.review.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)

print(pos_cnt)
print(neg_cnt)

# get_feature(df_neg['review'])

# #Transform each sentences in vector space

# vector = vectorizer.transform(df_neg['review'])
# vector_spaces = vector.toarray()

# print(vector_spaces)
# print(df_pos['review'].value_counts())

# df_pos['review'].str.cat(sep = ",")
# print(df_pos['review'])

# df_pos['review'] = df_pos['review'].astype(str)

# print(df_pos.dtypes)

# df_pos['review'] = df_pos['review'].astype('string')
# df_pos['sentiment'] = df_pos['sentiment'].astype('string')

# print(df_pos.dtypes)

# df_pos['review'].str.cat(sep = ',')

# print(df_pos['review'])

