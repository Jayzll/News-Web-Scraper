import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

# URL of the specific article
url = 'https://std.stheadline.com/realtime/article/2033642/%E5%8D%B3%E6%99%82-%E5%9C%8B%E9%9A%9B-%E7%89%B9%E6%9C%97%E6%99%AE%E7%95%B6%E9%81%B8%E7%BE%8E%E5%9C%8B%E7%B8%BD%E7%B5%B1-%E5%82%B3%E5%8F%8D%E8%8F%AF%E8%AD%B0%E5%93%A1%E9%AD%AF%E6%AF%94%E5%A5%A7%E6%88%96%E4%BB%BB%E5%9C%8B%E5%8B%99%E5%8D%BF-%E6%8C%81%E7%BA%8C%E6%9B%B4%E6%96%B0'

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping the headline
headline = soup.find('h1').get_text(strip=True)

# Scrape the image
picture = soup.find('img', class_='size-full w-100')['src'] if soup.find('img', class_='size-full w-100') else 'No image found'

# Scrape the category
category = soup.find('li', class_='nav-item active').get_text(strip=True) if soup.find('li', class_='nav-item active') else 'No category found'

# Find the author
author_tag = soup.find('div', class_='ssrcss-68pt20-Text-TextContributorName e8mq1e96')
author = author_tag.get_text(strip=True) if author_tag else 'No author found'

# Find all <p> tags and extract their text content
p_tags = soup.find_all('p')
body_text = ' '.join([p.get_text(strip=True) for p in p_tags])  # Join all paragraphs into one string

# Get today's date
today = date.today()

# Create a DataFrame with the article data
article_data = {
    'headline': headline,
    'picture': picture,
    'category': category,
    'author': author,
    'date': today,
    'body': body_text,  # Use the combined text here
    'url': url
}

# Convert to a DataFrame
df = pd.DataFrame([article_data])

# Save the DataFrame to a CSV file
csv_filename = f"{today}_article.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8')

# Display the DataFrame
df
