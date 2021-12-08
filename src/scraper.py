from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_benefits(wd):
	benefits = []
	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	for info in bs.find_all('td', class_='tags-th lfont m-3 py-3'):
		if info.p:
			benefits.append(info.p.text)
		else:
			benefits.append("")

	return benefits

def scrape_salaries(wd):
	salaries = []
	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	for salary_info in bs.find_all('div', class_='salary-info'):
		if salary_info.h6 and salary_info.p:
			temp = (salary_info.h6.text, salary_info.p.text)
			salaries.append(temp)
		else:
			salaries.append("Unknown")

	return salaries

def scrape_basic_info(wd):
	basic_info = []
	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	for company in bs.find_all('div', class_='media-body align-self-center'):
		basic_info.append(company.text.strip().replace(' \n', ': '))

	return basic_info


def scrape_links(wd):
	links = []
	html = wd.execute_script('return document.body.innerHTML')
	bs = BeautifulSoup(html, 'html.parser')

	for button in bs.find_all('td', class_='apply-th lfont m-3 py-3 d-none d-sm-table-cell'):
		if button.p.text == "Add":
			links.append("No Application Link Found")
		else:
			links.append(button.a['href'])

	return links

#################################################################################
website_url = "https://www.levels.fyi/internships/"
wd = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
wd.get(website_url)

print(f'Opening {website_url} for scraping...')
info = scrape_basic_info(wd)
print(f'Completed scraping basic info...')
salaries = scrape_salaries(wd)
print(f'Completed scraping salaries...')
benefits = scrape_benefits(wd)
print(f'Completed scraping benefits...')
links = scrape_links(wd)
print(f'Completed scraping links...')

with open('../data/scraped_text.txt', 'w', encoding='utf-8') as f:
	for i in range(len(info)):
		f.write(f'{info[i]} {salaries[i]} {benefits[i]}')
		f.write('\n')
f.close()
print('Scraped data written to file at /data/scraped_text.txt')

with open('../data/application_links.txt', 'w', encoding='utf-8') as f:
	for i in range(len(info)):
		f.write(f'{info[i]} Application -> {links[i]}')
		f.write('\n')
f.close()
print('Scraped application links written to file at /data/scraped_links.txt')

print('Scraping complete!')
wd.close()