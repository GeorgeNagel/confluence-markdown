""" Convert a Confluence export to markdown. """

import os
import shutil
import sys

from bs4 import BeautifulSoup
import html2text


if len(sys.argv) < 2:
    raise ArgumentError("Must be called with path to decompressed Confluence export folder.")

path_to_confluence_export = sys.argv[1]
confluence_export_parent_path, confluence_export_folder_name = os.path.split(path_to_confluence_export)
markdown_converted_folder_name = "%s-markdown" % confluence_export_folder_name 
path_to_markdown_converted = os.path.join(confluence_export_parent_path, markdown_converted_folder_name)

shutil.copytree(path_to_confluence_export, path_to_markdown_converted)

def make_hrefs_relative(text_content):
    soup = BeautifulSoup(text_content)
    for a in soup.findAll('a'):
        a['href'] = './%s' % a['href']
    return str(soup)

for root, dirs, files in os.walk(path_to_markdown_converted):
    for file in files:
        filename, extension = os.path.splitext(file)
        if not extension == '.html':
            continue

        path_to_html_file = os.path.join(root, file)
        print("Converting: %s" % path_to_html_file)
        markdown_text = ""
        with open(path_to_html_file, 'r') as fin:
            html_content = fin.read()

            # html_content = make_hrefs_relative(html_content)

            markdown_text = html2text.html2text(html_content)

        markdown_file = "%s.md" % filename
        path_to_markdown_file = os.path.join(root, markdown_file)
        with open(path_to_markdown_file, 'w') as fout:
            fout.write(markdown_text)

        os.remove(path_to_html_file)
print("Done!")
