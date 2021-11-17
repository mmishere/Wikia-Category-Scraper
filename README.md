## Wikia Category Scraper

Give the program a page of Wikia categories, and it'll create a .txt file for each category and insert all relevant article titles and links within it.

## Usage

1. Make sure you have Python3 installed.
2. Download `wikia_scraper.py` and `requirements.txt`.
3. Ppen the folder in your command prompt and type `pip3 install -r requirements.txt`.
4. `python3 wikia_scraper.py`.
5. It will ask for your input of a category URL (similar to `base_url/wiki/Special:Categories`). It doesn't matter if it starts with `https://` or not, but inputting a completely invalid URL will eventually cause problems.

If there are multiple category pages, then you'll have to do each of them manually. To speed this up, make sure that the site shows 500 categories per page, as that will give you a different URL (something like `base_url/wiki/Special:Categories?offset=&limit=500`).

This was tested on a few different Wikias, but if issues arise, feel free to report it on the [issues page](https://github.com/mmishere/Wikia-Category-Scraper/issues).

## Known issues
If you're using Windows, you might get this error while running the program:
`UnicodeEncodeError: 'charmap' codec can't encode character '\u200b' in position 1085: character maps to <undefined>`
To fix this, you can use WSL instead.

## License
GNU General Public License. Open source, but if you want to use it in something you're making, that also has to be open-source. For more details, see the License text.
