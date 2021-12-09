from gensim.summarization.bm25 import BM25
import formatter as formatter

def ranker(docs, query):
    corpus = [doc.split() for doc in docs]
    bm25 = BM25(corpus)
    query = query.split()
    scores = bm25.get_scores(query)
    
    return sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

documents = []
f = open('../data/formatted/documents.txt', 'r', encoding='utf-8')

for line in f.readlines():
    documents.append(line)
    print(line)
f.close()

ranked_docs = ranker(documents, "software engineer")
print(ranked_docs)
