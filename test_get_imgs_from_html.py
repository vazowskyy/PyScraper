import unittest 
from functions.get_images_from_html import get_images_from_html

class TestGetUrlsFrom(unittest.TestCase):
    def test_get_images_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_multiple_images(self):
        input_url = "https://crawler-test.com"
        input_body = '''
            <html>
                <body>
                    <img src="/img1.png">
                    <img src="https://example.com/img2.jpg">
                </body>
            </html>
        '''
        actual = get_images_from_html(input_body, input_url)
        expected = [
            "https://crawler-test.com/img1.png",
            "https://example.com/img2.jpg"
        ]
        self.assertEqual(actual, expected)


    def test_get_images_from_html_no_images(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><p>No images here!</p></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()