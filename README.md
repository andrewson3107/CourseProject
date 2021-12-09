# **CS410 Final Project: Job Postings Scraper and Ranker**

# Overview



# Implementation:

The first component of our application is `scraper.py` which is implemented in Python. It requires the packages BeautifulSoup4 and Selenium. Selenium is a paackage that allows the user to execute actions such as scrolling through the page or clicking on links. It is used to click on each outgoing application link on the job postings. After navigating to an individual application, BeautifulSoup4 is used to extract the html of the page. Afterwards, specific tags such as divs can be extracted further to retrieve the text contained within them. This is used to extract the application description text. 


# Execution:

Before running any scripts in the project, all dependencies must be installed. They can be installed via the following commands. The original project was written in Python 3.9.7. 
```
pip install -r requirements.txt

or 

python -m pip install -r requirements.txt
```

To execute the entire program, the scripts must be ran in the following order. 
```
1. scraper.py
2. formatter.py
3. ranker.py
```

### Contributions: