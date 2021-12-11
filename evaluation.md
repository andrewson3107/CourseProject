# Evaluation Method

To evaluate our results, `scraper.py` was ran on the following [link](https://www.linkedin.com/jobs/search?keywords=software%20engineering&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0) on 12/8/2021 to scrape a collection of 25 job postings. The outputted data was ran through `formatter.py` to format it into a bag of words representation. This output can be found in `data/evaluation/documents.txt`. 

On our end, we utilized the secondary output of `scraper.py` which consists of each job and a link to it's application page. This list can be found in `data/evaluation/application_links.txt`. Using the query "Experience with SQL databases", we individually went to every application and ranked them from 1 to 25 based on our own analysis and opinion of its relevance to the query. The process for ranking consisted of looking for as many matching words to database, data management, SQL, etc. and using that count to rank each application posting, while keeping mind factors such as document length. Our ranking can be found at `data/evaluation/human_ranking.txt`. 

Finally, we ran our ranker with the collection of documents in `data/evaluation/documents.txt` with the same query. This output can be found at `data/evaluation/program_ranking.txt`.
<br><br>


# Results:
- The top ranked application was matched between the human ranking and the BM25 ranking
- 5 out of the top 8 were matched between the human ranking and the BM25 ranking (6 postings were shared amongst the top 8 of both rankings)
    - We would have checked for the top 10 values, but the 9th and 10th ranked application links were removed from LinkedIn during the time of evaluation
- Beyond those matching 6/8, the ranking becomes pretty scrambled in order
- While the order is scrambled, most unrelated positions based off of the human ranking are near the bottom of the BM25 ranking
    - However, there are two outliers that were unrelated in human ranking but ended in the top 8 of the BM25 ranking: Mana Search (at 6) and VySystems (at 8)
