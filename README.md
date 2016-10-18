# Confluence GitHub wiki

Tools for converting Confluence wiki pages to [Markdown](https://daringfireball.net/projects/markdown/) for easy compatibility with GitHub wiki.

## Download an export of the relevant Confluence docs

Credit:
Steps submitted by user Dan Osburn here: https://answers.atlassian.com/questions/235590/export-pages-in-wiki-markup

1  In Confluence click 'Space Tools' in the bottom left and select 'Content Tools'.
2  Click the 'Export' tab > select 'HTML' > click 'Next'
3  Select 'Custom Export' > check the pages you want to export > click 'Export'
4  Wait for the pages to export, click the link to download.
5  Unzip the downloaded file. Move the resulting folder to the same directory as this file.

## Install this code

1. Clone the repo

    ```bash
    $ git clone git@github.com:GeorgeNagel/confluence-markdown.git
    # Move into the repo
    $ cd confluence-markdown

2. Create a Python virtual environment

    ```bash
    $ virtualenv -p python3 virtualenv
    $ source virtualenv/bin/activate
    ```

3. Install required packages

    ```bash
    (virtualenv)$ pip install -r requirements.txt
    ```

4. Convert your Confluence export to Markdown
    
    ```bash
    (virtualenv)$ python markdown.py path/to/confluence/export
    ```
