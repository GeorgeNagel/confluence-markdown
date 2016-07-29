import sys

from bs4 import BeautifulSoup
import requests
import html2text

url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
outfile_name = sys.argv[4]

# Make the request
response = requests.get(url, auth=(username, password))
assert response.status_code == 200, "Status code: %s" % response.status_code

# The css selector under which the relevant HTML is loaded
MAIN_CONTENT_SELECTOR = '#main-content'

# Parse the response html
soup = BeautifulSoup(response.content, 'html.parser')

# Get the element of interst
main_content_soup = soup.select(MAIN_CONTENT_SELECTOR)[0]
main_content_html_string = main_content_soup.decode_contents(formatter="html")

# Convert to markdown
markdown_text = html2text.html2text(main_content_html_string)

with open(outfile_name, 'w') as fout:
    fout.write(markdown_text)
