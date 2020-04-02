import pandas as pd 
import re


from nltk.tokenize import word_tokenize

data = pd.read_csv('computer_subset.csv')

for i in range(0, len(data)):
    raw_string = str(data.at[i,'body'])

    cleaned_string = re.sub('\\\\n', ' ', raw_string)

    data.at[i,'body'] = word_tokenize(cleaned_string)

data.to_csv('computer_subset_scraped_tokenized.csv')


