# Evaluation Method

To evaluate our results, `scraper.py` was ran on the following [link](https://www.linkedin.com/jobs/search?keywords=software%20engineering&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0) on 12/8/2021 to scrape a collection of 25 job postings. The outputted data was ran through `formatter.py` to format it into a bag of words representation. This output can be found in `data/evaluation/documents.txt`. 

On our end, we utilized the secondary output of `scraper.py` which consists of each job and a link to it's application page. This list can be found in `data/evaluation/application_links.txt`. Using the query "Experience with SQL databases", we individually went to every application and ranked them from 1 to 25 based on our own analysis and opinion of its relevance to the query. Our ranking can be found at `data/evaluation/human_ranking.txt`. 

Finally, we ran our ranker with the collection of documents in `data/evaluation/documents.txt` with the same query. This output can be found at `data/evaluation/program_ranking.txt`.
<br><br>


# Results:
- The ranker correctly ranked N documents
- The remaining documents were scrambled in order
