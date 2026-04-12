from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')

    imgs = []

    for img in soup.find_all('img'):
        imgs.append(urljoin(base_url,img.get('src')))


    return imgs