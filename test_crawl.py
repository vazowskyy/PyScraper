import unittest
from functions.crawl import normalize_url


class TestCrawl(unittest.TestCase):
    def test_normalize_url_https(self):
        input_url = "https://www.google.com/blog/path"
        actual = normalize_url(input_url)
        expected = "www.google.com/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_https_slash(self):
        input_url = "https://www.google.com/blog/path/test/"
        actual = normalize_url(input_url)
        expected = "www.google.com/blog/path/test"
        self.assertEqual(actual, expected)

    def test_normalize_url_http(self):
        input_url = "http://www.google.com/blog/path/test"
        actual = normalize_url(input_url)
        expected = "www.google.com/blog/path/test"
        self.assertEqual(actual, expected)

    def test_normalize_url_http_slash(self):
        input_url = "http://www.google.com/blog/path/test/"
        actual = normalize_url(input_url)
        expected = "www.google.com/blog/path/test"
        self.assertEqual(actual, expected)

    def test_normalize_url_nowww_http(self):
        input_url = "http://google.com/blog/path/test"
        actual = normalize_url(input_url)
        expected = "google.com/blog/path/test"
        self.assertEqual(actual, expected)

    def test_normalize_url_nowww_http_slash(self):
        input_url = "http://google.com/blog/path/test"
        actual = normalize_url(input_url)
        expected = "google.com/blog/path/test"
        self.assertEqual(actual, expected)

    def test_normalize_url(self):
        input_url = "http://test.pl"
        actual = normalize_url(input_url)
        expected = "test.pl"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()