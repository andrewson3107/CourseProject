# **CS410 Final Project: Job Postings Scraper and Ranker**

# Overview
Our project is an application that allows the user to scrape job postings from LinkedIn and rank the postings based on a search query. This can be used to narrow down more specifics based on the text of a job description or the qualifications needed for the job. 


# Backend Implementation:
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

Defines a function accepts a list of documents and a query that returns a sorted list of indexes of the documents based on the ranking. Using that function, ranks the formatted documents in `data/formatted/documents.txt` based off a query term and outputs the sorted list of indexes. Using the raw list of application links, the ranked list of application links is created using the sorted list of indexes at `data/ranked/ranked_application_links.txt`.

# Frontend Implementation:
The frontend for this application is written with Flask. All of the files related to the frontend can be found in `frontend_flask/`.

`frontend_flask/` contains the following:
- `app.py`: Handles a `GET` request to the `rank` endpoint to allow for ranking. This passes in the parameter `query` containing the user inputted search query. The frontend runs the program by importing all `src/` files and running them individually before returning a json output of the ranked job postings. 
- `templates/`: A directory containing HTML files that are used to dictate the appearance of the frontend. These are loaded onto the flask application in via `render_template` in `app.py` 


# Setup:
The following dependencies are required:
- Python 3.8
- Selenium
- beautifulsoup4
- gensim 3.8.3
- flask

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
To execute the entire program without the frontend, the scripts must be ran in the following order. 

```
1. scraper.py
2. formatter.py
3. ranker.py
```

The final ranking of the program can be found under `data/ranking/ranking.txt`. Note: it is a zero-index ranking, so line 1 in the ranking will refer to document 0 in the collection.

To execute the program with the provided frontend:
- Navigate into `frontend_flask/`
- Run `flask run` or `python -m flask run`
- Navigate to http://127.0.0.1:5000/ on a browser
- Enter a query in the text box and hit search

# Contributions:
Andrew28:
- `scraper.py`
- `formatter.py`