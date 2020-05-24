#! /usr/bin/python3

''' Script which opens the classic 2048 game in the web browser
and plays by choosing random directions and displays the score in the end
Usage: open the terminal and run the following command- python3 play2048.py
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

def play2048():

	# Launch the 2048 game in the web browser
	driver = webdriver.Firefox()
	driver.maximize_window()

	driver.get('https://play2048.co/')
	
	# Store the valid key presses in a list
	dir_keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

	elem = driver.find_element_by_tag_name('html')

	# Loop till the game is not over
	while driver.find_elements_by_css_selector('.game-message > p:nth-child(1)')[0].text.strip() == "":
		elem.send_keys(dir_keys[random.randint(0,3)])
		time.sleep(0.1)
	
	# Fetch the score of the player
	score = driver.find_element_by_css_selector('.score-container').text
	
	print(f'Game over! You scored {score} points.')

		
def main():
	play2048()		
		
if __name__ == '__main__':
	main()
