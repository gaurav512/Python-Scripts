#! /usr/bin/python3

# Author: gaurav512

''' Check for the price of an item at www.amazon.in and send a mail to the specified email address 
if the price drops below a certain amount
Item considered: Set of Harry Potter Books
Task: Send a mail if price is below Rs. 2250
'''

import requests, bs4, smtplib, unidecode

def send_mail(title, price):

	# Connect to the gmail smtp server
	conn = smtplib.SMTP('smtp.gmail.com', 587)
	conn.ehlo()
	conn.starttls()
	
	# Login using your credentials (Replace the parameters with your email and password respectively)
	conn.login('xxxxxxx@gmail.com', 'xxxxxxxxxxx')
	
	# Send mail to the email address (first parameter: From address, second parameter: To address)
	conn.sendmail('xxxxxxx@gmail.com', 'xxxxxxxx@xxx.xxx', f'Subject: Amazon Price Drop\n\nHey, the price of {title} is now Rs. {price}\nCheck it out.')
	print('You mail has been sent')
	
	
def check_price():

	url = 'https://www.amazon.in/Harry-Potter-ChildrenS-Paperback-Boxed/dp/1408856778/'

	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
	
	# Fetch the respective page details
	page = requests.get(url, headers=headers)
	
	# Raise an exception if page cannot be loaded
	try:
		page.raise_for_status()
	except:
		print('Link is broken')
		return
	# Create a beautiful soup object
	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	
	# Fetch title
	title = soup.find(id='productTitle').get_text().strip()
	title = unidecode.unidecode(title)
	
	# Fetch price
	price = soup.select('.inlineBlock-display')[0].text
	price = price[2:]
	price = float("".join(price.split(',')))
	
	# If price drops below 2250, call the send_mail function
	if price <= 2250:
		send_mail(title, price)
		
		
def main():
	check_price()

if __name__ == '__main__':
	main()

