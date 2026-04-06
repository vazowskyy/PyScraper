from bs4 import BeautifulSoup


def get_heading_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    h1 = soup.find('h1')
    h1 = soup.h1.get_text() if h1 else ""
    if h1:
        return h1 

    h2 = soup.find('h2')
    if h2:
        return h2

    return h1 
