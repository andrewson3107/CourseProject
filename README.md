# **CS410 Final Project: Job Postings Scraper and Ranker**

# Overview



# Implementation:
`scraper.py`

Scrapes a variable number of job postings from a LinkedIn job posting page. Any job postings page can be used. The link used for this program can be found [here](https://www.linkedin.com/jobs/search?keywords=software%20engineering&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0). 

There are two components to the scraper. The first utilizes Selenium to click each seperate job in the scrolling sidebar. The second utilizes BeautifulSoup4 to scrape the text from each seperate job posting. 

`scraper.py` outputs two text files:
- `application_links.txt` which contains the title of each job and a link to that specific job posting. Located in `data/raw/`
- `scraped_text.txt` which contains the raw text of each job posting. This data may vary based on job posting but typically includes basic job info, qualifications, and requirements.

`formatter.py`

Formats the raw data outputted from `scraper.py` with the following criteria:
- Lower cases all words.
- Removes all links.
- Removes all non alphabetic characters excluding + (for C++), # (for C#), and ' (for contractions).
- Removes stop words such as "the" and "we".
- Corrects extra spaces and reduces them to a single space.

`ranker.py`


# Setup:
The following dependencies are required:
- Python 3.8
- Selenium
- beautifulsoup4
- gensim 3.8.3

In order to install Gensim, Microsoft Visual C++ 14.0 or greater is required. It can be downloaded from the link provided below.

https://visualstudio.microsoft.com/visual-cpp-build-tools/

These dependencies can be installed by running the following commands from the root directory of the project
```
pip install -r requirements.txt

or 

python -m pip install -r requirements.txt
```

Additionally, in order for Selenium to function properly with Chrome, the proper drivers must be installed and placed inside `drivers/`. The drivers can be downloaded from the link provided below. Pay attention to what version of Chrome is installed on your machine and select the according drivers for your operating system.  

https://chromedriver.chromium.org/downloads


# Execution:
To execute the entire program, the scripts must be ran in the following order. 

```
1. scraper.py
2. formatter.py
3. ranker.py
```

The final ranking of the program can be found under `data/ranking/ranking.txt`


# Contributions:
Andrew28:
- `scraper.py`
- `formatter.py`