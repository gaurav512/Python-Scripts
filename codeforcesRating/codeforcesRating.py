#! /usr/bin/pyhton3

# Author: gaurav512

''' Script written to scrape basic information about a 
Codeforces profile given the user id
Usage: Enter the userid as command line argument OR as the input
after running the following in terminal- python3 codeforces.py [userid]
'''

import requests, bs4, sys

def getDetails(userid):

	url = 'http://www.codeforces.com/profile/'+userid
	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	
	res = requests.get(url, headers=headers)
	try:
		res.raise_for_status()
	except:
		print('Cannot access codeforces')
		return
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	# Getting the rating of the user	
	title = soup.select('.user-rank > span:nth-child(1)')
	if not title:
		print(f'User \'{userid}\' not found')
		return None
	title = title[0].text
	print('Title:\t\t',title)
	
	# Getting the name and place of the user (if updated on profile)
	elem = soup.select('.main-info > div:nth-child(3) > div:nth-child(1)')
	if elem:
		content = elem[0].text.split(',')
		name = content[0]
		print('Name:\t\t',name)
		if len(content) > 1:
			place = ','.join(content[1:]).lstrip()
			print('Place:  \t', place)
	
	# Getting organization of the user (if updated on profile)
	elem2 = soup.select('.main-info > div:nth-child(3) > div:nth-child(2)')
	if elem2:
		organization = elem2[0].text
		pos = organization.find(' ')
		print('Organization:\t', organization[pos+1:])
	
	# If the user is unrated then return back
	if title.strip() == 'Unrated':
		return None
	
	# Following code snippet takes care of the inconsistent css selectors on the Codeforces site due to display of badges in some profiles	
	rating_selector = '.info > ul:nth-child(2) > li:nth-child(1) > span:nth-child(2)' 
	if soup.select('div.badge:nth-child(1) > img:nth-child(1)'):
		rating_selector = rating_selector[:21]+'3'+rating_selector[22:]
	
	# Fetch the rating of the user
	rating = soup.select(rating_selector)[0].text
	print('Rating:\t\t', rating)
	
	# Fetch the highest title achieved by the user
	highestTitle = soup.select('span.smaller > span:nth-child(1)')[0].text
	print('Highest Title:\t', highestTitle[:-2].title())
	
	# Fetch the highest rating achieved by the user
	highestRating = soup.select('span.smaller > span:nth-child(2)')[0].text
	print('Highest Rating:\t', highestRating)
	

def main():
	if len(sys.argv) > 1:
		userid = sys.argv[1]
	else:
		userid = input()
	getDetails(userid)


if __name__ == '__main__':
	main()
