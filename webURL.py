"""
Web Scrapper Specification:
    Target URL: https://www.bbc.com/news
    Goal: Extract and display the latest news headliens.

    What kind of data?
        Data that are within header tags like <h1>, <h2> or <h3> along with specific CSS classes.

    Data Output:
        Headlines List: Display a list of headlines in a numbered format.
        *Add more details* for example: lints to the full articles.

    Handling Errors: 
        Would be mainly looking at status codes to handle the errors.
        
"""



import requests
from bs4 import BeautifulSoup


url = "https://www.bbc.com/news"
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('a')

    for idx, headline in enumerate(headlines, 1):
        title = headline.get_text(strip=True)
        
        link = headline['href']

        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link

        print(f'{idx}. {title} [{link}]')
else:   
    print(f'Failed to retrieve content from {url}. Status code: {response.status_code}')

