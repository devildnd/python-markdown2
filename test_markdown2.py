import unittest
from markdown2 import markdown

class TestMarkdown2(unittest.TestCase):
    def test_markdown(self):
        self.assertEqual(markdown('# Hello'), '<h1>Hello</h1>')
        self.assertEqual(markdown('*bold*'), '<strong>bold</strong>')

if __name__ == '__main__':
    unittest.main()
