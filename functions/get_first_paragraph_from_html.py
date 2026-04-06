from bs4 import BeautifulSoup


def get_first_paragraph_from_html(html):
    p = soup.main.p 

    if p:
        p = p.get_text()
    else: 
        p = soup.p.extract_text if soup.p else ""
    return p
    