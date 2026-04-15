from bs4 import BeautifulSoup

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    main = soup.find('main')

    if main:
        p = main.find('p')
    else:
        p = soup.find('p')

    if p:
        return p.get_text(strip=True)
    
    return ""