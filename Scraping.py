""" The text in the data set we use contains a lot of html-tags, and we are not
interested in those tags. Therefore, I scrape the texts to get rid of the tags.
"""

from bs4 import BeautifulSoup as soup
import pandas as pd

data = pd.read_csv('dsjVoxArticles.tsv', sep='\t')

error_frame = pd.DataFrame(columns=['title','author','published_date','updated_on','slug','blurb','body'])
for i in range(0, len(data)):
    raw_text =data.at[i,'body']

    try:
        text = soup(raw_text,'html.parser')
    except TypeError:
        error_frame.append(data.iloc[i])
        continue
    data.at[i,'body'] = soup.get_text(text)

data.to_csv('dsjVoxArticles_scraped.tsv', sep = '\t')

data.to_csv('errors_dsjVoxArticles_scraped.tsv', sep = '\t')


