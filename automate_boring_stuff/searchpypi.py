# Searchpypi.py - Opens several search results on pypi.org

import requests, sys, webbrowser, bs4

print('Searchin...')
res = requests.get("https://pypi.org/search/?q=" + ''.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
print(soup.select('div'))
link_elems = soup.select('a.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i]['href']
    webbrowser.open(url_to_open)
