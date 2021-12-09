from gensim.summarization.bm25 import BM25

def read_documents():
    documents = []
    f = open('../data/formatted/documents.txt', 'r', encoding='utf-8')

    for line in f.readlines():
        documents.append(line)
    f.close()

    return documents

def rank_documents(documents, query):
    corpus = [doc.split() for doc in documents]
    bm25 = BM25(corpus)
    query = query.split()
    scores = bm25.get_scores(query)
    ranked_docs = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    return ranked_docs 

def read_links():
    links = []
    f = open('../data/raw/application_links.txt', 'r', encoding='utf-8')

    for line in f.readlines():
        links.append(line)
    f.close()

    return links


def write_ranking(ranked_docs, links):
    ranked_links = [links[i] for i in ranked_docs]
    f = open('../data/ranked/documents.txt', 'w', encoding='utf-8')
    for link in ranked_links:
        f.write(f'{link}')
    f.close()
    
##########################################################
# This variable can be modified to any query
query = "Experience with SQL databases"

documents = read_documents()
print("Initializing documents from text file complete.")

links = read_links()
print("Initializing application links from text file complete.")

ranked_docs = rank_documents(documents,query)
print("Ranking complete.")

write_ranking(ranked_docs, links)
print("Ranking written to file located at ../data/ranked/documents.txt.")
