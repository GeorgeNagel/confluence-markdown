""" Rename a page in a Markdown-converted Confluence export. """
import os
import re
import sys

from bs4 import BeautifulSoup


if len(sys.argv) < 3:
    raise ArgumentError(
        "Must be called with path to the Markdown-converted"
        " Confluence export folder and the name of the file to convert."
    )

path_to_markdown_converted = sys.argv[1]
file_to_rename = sys.argv[2]
new_filename = sys.argv[3]

path_to_file = os.path.join(path_to_markdown_converted, file_to_rename)
new_path = os.path.join(path_to_markdown_converted, new_filename)
os.rename(path_to_file, new_path)

def rename_markdown_link(text_content, old_path, new_path):
    return re.sub(old_path, new_path, text_content)

# Now that we've renamed it, we also have to rename any links referencing the file.
for root, dirs, files in os.walk(path_to_markdown_converted):
    for file in files:
        filename, extension = os.path.splitext(file)
        if not extension == '.md':
            continue

        path_to_markdown_file = os.path.join(root, file)
        with open(path_to_markdown_file, 'r', encoding='utf-8', errors='ignore') as fin:
            text_content = fin.read()
            updated_content = rename_markdown_link(text_content, file_to_rename, new_filename)

        with open(path_to_markdown_file, 'w') as fout:
            fout.write(updated_content)

print("Renamed %s to %s" % (file_to_rename, new_filename))
