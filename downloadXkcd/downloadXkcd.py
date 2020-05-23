#! /usr/bin/python3

# Author: gaurav512

''' Script to download ALL the comics from xkcd.com and 
save them in a folder 'xkcd' in the current working directory
Usage: Run the following command on terminal- python3 downloadXkcd.py
'''

import requests, bs4, os

def download():
	
	# Header to save my user agent
	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	
	generic_url = 'https://xkcd.com'
	url = generic_url
	
	# New folder in the current working directory to save all the comics
	os.makedirs('xkcd')
	
	# Download all xkcd comics in a loop
	while True:
	
		# Fetch the xkcd page
		page = requests.get(url, headers=headers)
		
		try:
			page.raise_for_status()
		except:
			print('Some link was broken')
			return
		
		soup = bs4.BeautifulSoup(page.text, 'html.parser')
		
		# Find link of the previous xkcd comic
		prev = soup.select('a[rel="prev"]')[0].get('href')
		
		# Find the url of current image and download
		img = soup.select('#comic > img:nth-child(1)')
		imgsrc = 'http:' + img[0].get('src')
		image = requests.get(imgsrc, headers=headers)
		
		try:
			image.raise_for_status()
		except:
			print('Image can\'t be opened')
			return
		
		fileName = str(int(prev[1:-1])+1) # Keep filename same as comic number
		print(f'Downloading image https://xkcd.com/{fileName}.png ....')
		
		# Open a new image file
		imageFile = open(f'xkcd/{fileName}.png', 'wb')
		for chunk in image.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
		# Check if we have reached the first ever xkcd comic
		if prev == '#':
			break
		url = generic_url + prev
		
		
def main():
	download()

if __name__ == '__main__':
	download()
