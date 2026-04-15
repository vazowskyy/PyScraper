import requests


def get_html(url):

    try: 
        r = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
        status_code = r.status_code
        if status_code > 400:
            return f"Error: Code {status_code}"
        elif r.headers['content-type'] != 'text/html':
            return f"Error: Invalid headers: {r.headers['content-type']}" 
        
        return r.text

    except Exception as e:
        return f"Error: {e}"
