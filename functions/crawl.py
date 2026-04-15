from urllib.parse import urlsplit, urljoin


def normalize_url(input_url):
    url_obj = urlsplit(input_url)
    
    netlock = url_obj.netloc
    
    if len(url_obj.path) == 0:
        return netlock
    
    path = url_obj.path if url_obj.path[-1] != '/' else url_obj.path[:-1]

    return netlock + path
