# Indeed.com Job Description Word Counts for Job Apps

import requests
import numpy as np
from bs4 import BeautifulSoup
import collections
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
stop = stopwords.words('english')


URL = input('Please provide the URL: ')
existinglist = {}

# ## 2. Run below function:
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="jobDescriptionText")
all_text = results.text

all_text = all_text.replace('[^\w\s]',' ')
punc = '''!(')-[]{};:'"\,<>./?@#$%^&*`_~'''
nums  = '1234567890'

# Removing punctuations in string
# Using loop + punctuation string
for ele in all_text:
    if ele in punc or ele in nums:
        all_text = all_text.replace(ele, " ")

all_text = all_text.replace("\n", " ")


alltext = all_text.split(' ')

alltext = ' '.join(alltext)


textnostop = [word for word in alltext.split(' ') if word not in stop]


for word in textnostop:
    if len(word) == 0 or word == '':
        textnostop.remove(word)
for word in textnostop:
    if word not in existinglist.keys():
        existinglist[word] = 1
    else:
        existinglist[word] += 1
nogos = ['', 'you', 'https', 'we', 'We', 'one', 'us', 'role', 'us', 'com', 'work', 'within', 'working', 'company',
         'career', 'make', 'www', 'Our', 'our', 'at', 'At']

for nogo in nogos:
    if nogo in existinglist.keys():
        del existinglist[nogo]

final_list = dict(sorted(existinglist.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:30])
final_list_correct = sorted(final_list.items(), key = lambda kv:(kv[1], kv[0]))

print(dict(sorted(existinglist.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)))
