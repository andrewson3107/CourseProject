from selenium import webdriver
from bs4 import BeautifulSoup
import time

# def scrape_benefits(wd):
# 	benefits = []
# 	html = wd.execute_script('return document.body.innerHTML')
# 	bs = BeautifulSoup(html, 'html.parser')

# 	for info in bs.find_all('td', class_='tags-th lfont m-3 py-3'):
# 		if info.p:
# 			benefits.append(info.p.text)
# 		else:
# 			benefits.append("")

# 	return benefits

# def scrape_salaries(wd):
# 	salaries = []
# 	html = wd.execute_script('return document.body.innerHTML')
# 	bs = BeautifulSoup(html, 'html.parser')

# 	for salary_info in bs.find_all('div', class_='salary-info'):
# 		if salary_info.h6 and salary_info.p:
# 			temp = (salary_info.h6.text, salary_info.p.text)
# 			salaries.append(temp)
# 		else:
# 			salaries.append("Unknown")

# 	return salaries

# def scrape_basic_info(wd):
# 	basic_info = []
# 	html = wd.execute_script('return document.body.innerHTML')
# 	bs = BeautifulSoup(html, 'html.parser')

# 	for company in bs.find_all('div', class_='media-body align-self-center'):
# 		basic_info.append(company.text.strip().replace(' \n', ': '))

# 	return basic_info


# def scrape_links(wd):
# 	links = []
# 	html = wd.execute_script('return document.body.innerHTML')
# 	bs = BeautifulSoup(html, 'html.parser')

# 	for button in bs.find_all('td', class_='apply-th lfont m-3 py-3 d-none d-sm-table-cell'):
# 		if button.p.text == "Add":
# 			links.append("No Application Link Found")
# 		else:
# 			links.append(button.a['href'])

# 	return links

# #################################################################################
# website_url = "https://www.levels.fyi/internships/"
# wd = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
# wd.get(website_url)

# print(f'Opening {website_url} for scraping...')
# info = scrape_basic_info(wd)
# print(f'Completed scraping basic info...')
# salaries = scrape_salaries(wd)
# print(f'Completed scraping salaries...')
# benefits = scrape_benefits(wd)
# print(f'Completed scraping benefits...')
# links = scrape_links(wd)
# print(f'Completed scraping links...')

# with open('../data/scraped_text.txt', 'w', encoding='utf-8') as f:
# 	for i in range(len(info)):
# 		f.write(f'{info[i]} {salaries[i]} {benefits[i]}')
# 		f.write('\n')
# f.close()
# print('Scraped data written to file at /data/scraped_text.txt')

# with open('../data/application_links.txt', 'w', encoding='utf-8') as f:
# 	for i in range(len(info)):
# 		f.write(f'{info[i]} Application -> {links[i]}')
# 		f.write('\n')
# f.close()
# print('Scraped application links written to file at /data/scraped_links.txt')

# print('Scraping complete!')
# wd.close()

titles = []
descriptions = []
urls = []

def write_to_file():
	f = open('../data/application_links.txt', 'w', encoding='utf-8')
	j = open('../data/scraped_text.txt', 'w', encoding='utf-8')

	for i in range(len(titles)):
		f.write(f'{titles[i]} -> {urls[i]}')
		f.write('\n')
		j.write(f'{descriptions[i]}')
		j.write('\n')

	f.close()
	j.close()

def scrape_posting(wd, url):
	wd.get(url)
	time.sleep(5)

	if "authwall" in wd.current_url:
		scrape_posting(wd,url)
		return


	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	title = bs.find('a', class_='topcard__org-name-link topcard__flavor--black-link')
	description = bs.find('div', class_='description__text description__text--rich')
	titles.append(title.text.strip())
	descriptions.append(description.text.strip())
	urls.append(url)

def crawl_sidebar(wd):
	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	sidebar = bs.find('ul', class_='jobs-search__results-list')

	i = 1

	listings = sidebar.find_all('li')
	for listing in listings:
		url = listing.div.a['href']
		scrape_posting(wd, url)
		print(f'Scraping in progress...    {i}/{len(listings)}')
		i += 1
	
	print('Scraping Complete.')


website_url = "https://www.linkedin.com/jobs/search?keywords=software%20engineering&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0"
wd = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
wd.get(website_url)

crawl_sidebar(wd)
write_to_file()
wd.close()



