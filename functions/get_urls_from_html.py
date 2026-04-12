from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')

    links = [] 

    for link in soup.find_all('a'):
        links.append(urljoin(base_url ,link.get('href')))
    
    return links