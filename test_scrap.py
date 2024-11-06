import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

# URL of the specific article
url = 'https://www.bbc.co.uk/news/articles/cd0gj0z7729o'

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping the headline
headline = soup.find('h1').get_text(strip=True)

# Find the author using the provided class
author_tag = soup.find('div', class_='ssrcss-68pt20-Text-TextContributorName e8mq1e96')
if author_tag:
    author = author_tag.get_text(strip=True)
else:
    author = 'No author found'

body_tag = soup.find('div', class_='ssrcss-7uxr49-RichTextContainer e5tfeyi1')
if body_tag:
    body = body_tag.get_text(strip=True)
else:
    body = "No Body Found"
# Get today's date
today = date.today()

# Create a DataFrame with the article data
article_data = {
    'headline': headline,
    'author': author,
    'url': url,
    'date': today,
    'body': body
}

# Convert to a DataFrame
df = pd.DataFrame([article_data])

# Save the DataFrame to a CSV file
csv_filename = str(today) + '_bbc_article.csv'
df.to_csv(csv_filename, index=False)

# Display the DataFrame
df
