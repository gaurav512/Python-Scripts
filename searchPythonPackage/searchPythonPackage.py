#! /usr/bin/python3

''' Searches for the keywords given as command line arguments on the website 
https://pypi.org/ and opens the top 5 links in the browser 
Usage: Run the following in the terminal- python3 search-python-package.py [keywords]
[keywords] refers to one or more command line arguments
'''

import webbrowser, requests, bs4, sys

def open_links(keyword):
	
	url = 'https://pypi.org/search/?q=' + keyword
	
	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	res = requests.get(url, headers=headers)
	
	try:
		res.raise_for_status()
	except:
		print('Link is broken')
		return
	
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	linkElements = soup.select('.package-snippet')
	
	if not linkElements:
		print('No matching package found')
		return
	
	numTabs = min(len(linkElements), 5)
	
	for i in range(numTabs):
		packageURL = 'https://pypi.org' + linkElements[i].get('href')
		print(f'Opening {packageURL}')
		webbrowser.open(packageURL)
		
def main():
	if len(sys.argv) > 1:
		keyword = " ".join(sys.argv[1:])
		open_links(keyword)
	else:
		print('Please enter the keyword as command line args')
			
if __name__ == '__main__':
	main()
