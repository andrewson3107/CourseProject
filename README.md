# **CS410 Final Project: Job Postings Scraper and Ranker**

# Overview



# Implementation:
`scraper.py`
`formatter.py`
`ranker.py`


# Setup:

The following dependencies are required:
- Python 3.9
- Selenium
- BeautifulSoup
- numpy

The dependencies can be installed by running the following commands from the root directory of the project. 
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

### Contributions: