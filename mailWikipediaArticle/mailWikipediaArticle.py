#! /usr/bin/python3

# Author: gaurav512

''' This script fetches the gist of the 'Today's Article' section from Wikipedia and 
mails it to the pre-determined e-mail address
Usage: Change the email and password fields in this script and then run the following
on the terminal: python3 mailWikiArticle.py
'''

import requests, bs4, smtplib, unidecode

def send_mail():

	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	# Getting data from the Wikipedia main page
	re = requests.get('https://en.wikipedia.org/wiki/Main_Page', headers=headers)

	# Raising a traceback in case there is any exception while accessing the site
	try:
		re.raise_for_status()
	except:
		print('Link is broken / Cannot open link')
		return

	soup = bs4.BeautifulSoup(re.text, 'html.parser')

	# Fetching the Today's Article section
	elem = soup.select('#mp-tfa > p:nth-child(2)')

	# Removing unnecessary characters from the data and then converting all non-ASCII characters to their nearest ASCII equivalent using the unidecode module
	gist = elem[0].text[:-19]
	gist = unidecode.unidecode(gist)

	# Connecting to the gmail smtp server and starting connection
	conn = smtplib.SMTP('smtp.gmail.com', 587)
	conn.ehlo()
	conn.starttls()

	# Login using your credentials (Replace the parameters with your email and password respectively)
	conn.login('xxxxxxx@gmail.com', 'xxxxxxxxxxx')
	
	# Send mail to the email address (first parameter: From address, second parameter: To address)
	conn.sendmail('xxxxxxxxxxxxx@gmail.com', 'xxxxxxxxx@xxx.xxx', f'Subject: Today\'s Wikipedia Article\n\n{gist}')
	
	conn.quit()

def main():
	send_mail()

if __name__ == '__main__':
	main()
