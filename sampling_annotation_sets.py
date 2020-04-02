import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

data = pd.read_csv('computer_subset_scraped_tokenized.csv')

leave, annotate = train_test_split(data,test_size = 110, random_state=90, stratify=data['month'])

print('Texts to annotate: ', len(annotate))
print('Texts that will not be annotated: ', len(leave))

annotate, common_texts = train_test_split(annotate, test_size = 10, random_state=20)

annotate_diana, annotate_edward = train_test_split(annotate, test_size = 50, random_state=42)

annotate_diana = shuffle(pd.concat([annotate_diana, common_texts]))

annotate_edward = shuffle(pd.concat([annotate_edward, common_texts]))



print('Number of texts Edward will annotate: ', len(annotate_edward))

print('Number of texts Diana will annotate: ', len(annotate_diana))

leave.to_csv('computer_subset_unannotated.csv')

annotate_diana.to_csv('computer_subset_annotate_diana.csv')

annotate_edward.to_csv('computer_subset_annotate_edward.csv')

common_texts.to_csv('computer_subset_annotate_common')