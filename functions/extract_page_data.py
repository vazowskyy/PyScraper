from functions.get_first_paragraph_from_html import get_first_paragraph_from_html
from functions.get_heading_from_html import get_heading_from_html
from functions.get_images_from_html import get_images_from_html
from functions.get_urls_from_html import get_urls_from_html
from functions.crawl import normalize_url

def extract_page_data(html, page_url):
    url = normalize_url(page_url)
    extracted_links = get_urls_from_html(html, page_url)
    images = get_images_from_html(html, page_url)
    headings = get_heading_from_html(html)
    paragraph  = get_first_paragraph_from_html(html)

    result = {
        "url" : page_url,
        "heading" : headings,
        "first_paragraph" : paragraph,
        "outgoing_links" : extracted_links,
        "image_urls" : images
    }

    print(result)

    return result 


