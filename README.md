# Confluence Markdown

Convert content of a Confluence page to markdown

## Install

1. Clone the repo

	```bash
	$ git clone git@github.com:GeorgeNagel/confluence-markdown.git
	# Move into the repo
	$ cd confluence-markdown

2. Create a Python virtual environment

	```bash
	$ virtualenv virtualenv
	$ source virtualenv/bin/activate
	```

3. Install required packages

	```bash
	$ pip install -r requirements.txt
	```

4. Run against a url

	```bash
	(virtualenv)$ python convert.py "http://confluence-page-to-convert.com" username password outfilename.md
	```
