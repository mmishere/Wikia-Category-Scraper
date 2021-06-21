## Wikia Category Scraper

Give the program a page of Wikia categories, and it'll create files for each category and insert all article titles and links within it.

## Usage

Make sure you have Python3 installed.
Download `wikia_scraper.py` and `requirements.txt`.
Then, open the folder in your command prompt and type `pip3 install -r requirements.txt`.
After that, `python3 wikia_scraper.py`.
It will ask for your input of a base URL (the site's main URL) and a category URL (something similar to `base_url/wiki/Special:Categories`).

If there are multiple category pages, then you'll have to do each of them manually. To speed this up, make sure that it's showing 500 categories per page, as that will give you a different URL (something like `base_url/wiki/Special:Categories?offset=&limit=500`).
