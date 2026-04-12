import unittest 
from functions.get_urls_from_html import get_urls_from_html

class TestGetUrlsFrom(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><a href="/about">About</a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/about"]
        self.assertEqual(actual, expected)


    def test_get_urls_from_html_multiple_links(self):
        input_url = "https://crawler-test.com"
        input_body = '''
            <html>
                <body>
                    <a href="/contact">Contact</a>
                    <a href="https://example.com">External</a>
                </body>
            </html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        expected = [
            "https://crawler-test.com/contact",
            "https://example.com"
        ]
        self.assertEqual(actual, expected)


    def test_get_urls_from_html_no_links(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><p>No links here!</p></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()