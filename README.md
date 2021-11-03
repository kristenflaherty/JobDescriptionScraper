# JobDescriptionScraper
Overview
-
Web scraper that identifies the most frequently used words in an Indeed job description to help prospective employees better tailor their job applications before submitting to Indeed.com jobs. *This only words for Indeed job postings!!!*

To run:
-
There are two options to run this scraper: **Jupyter notebook** where you input the URL of the Indeed job posting and can visualize the distribution of most frequently used words, OR a **Python file** where you can run on your own computer and input the URL of the Indeed job posting and receive a list of most frequently used words and their word counts.

For BOTH methods, you must download the following libraries:
- Requests
- bs4 for BeautifulSoup
- String
- Numpy
- Matplotlib.pyplot
- Collections
- Ntlk

**Input**: URL of Indeed Job Description

**Output**: list of most frequenly used words, in order of most used to least used
