from bs4 import BeautifulSoup as soup
import urllib
from urllib.request import urlopen as Ureq
import requests
import csv
import sys


#define variables for the script
base_url_main_page = "https://pitchfork.com/reviews/albums/"
base_url_album_pages = "https://pitchfork.com"

page_numbers = 1
headers = "Album | Artist | Score | Author | Genre | Review Date \n"

#open csv file
with open('albums_complete_second_half.csv', 'wb') as csvfile:
	csvfile.write((headers).encode('utf8'))

	items = []

#Iterate through every page on https://pitchfork.com/reviews/albums/
	while(True):
		url = (base_url_main_page+"?page="+str(page_numbers))

		#iterate through until no page is found. Ignore other HTTP response errors
		try:
			response = Ureq(url)
		except urllib.error.HTTPError as e:
			error_message = e.read()
			if e.getcode() == 404:
				sys.exit("No page found")
			else:
				print(error_message)
		else:
			page_html = response.read()
			page_soup = soup(page_html, "html.parser")

			url_names = page_soup.findAll("div",class_= "review")

			count = 0
			#enter urls of album reviews
			for item in url_names:
				url_name = url_names[count].a["href"]

				album_url = (base_url_album_pages+url_name)

				#ignore HTTP response errors
				try: 
					album_response = Ureq(album_url)
				except urllib.error.HTTPError as ea:
					album_error_message = ea.read()
					print(album_error_message)
				else:
					album_page_html = album_response.read()
					album_page_soup = soup(album_page_html, "html.parser")

					#scrape data from reviews
					album_name = album_page_soup.h1.text
					artist_name = album_page_soup.h2.ul.li.get_text()
					score = album_page_soup.body.find('span',class_ = 'score').text
					author = album_page_soup.find('a',class_ = 'authors-detail__display-name').text
					if 'genre-list__item' in str(album_page_soup):
						genre = album_page_soup.find('li',class_ = 'genre-list__item').text
					else:
						genre = "None"
					review_date = album_page_soup.find('time', class_ = 'pub-date')['datetime']

					#enter this data into the csv file
					csvfile.write('{}\n'.format('|'.join([album_name, artist_name, score, author, genre, review_date])).encode('utf8'))
					items.append([album_name, artist_name, score, author, genre, review_date])
					print(album_name)
				count+=1

		#log album names to show progress and status on script while it is running
		print("\n\n\n page number:" + str(page_numbers) + "\n\n\n")
		page_numbers+=1	
	



