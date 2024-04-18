from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
import pickle

class InvertedIndex: # AiAgent ChatGPT
    def __init__(self):
        self.documents = []
        self.inverted_index = defaultdict(list)
        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def fit_transform(self, documents):
        self.documents = documents
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
        self._build_inverted_index()

    def _build_inverted_index(self):
        for docid, document in enumerate(self.documents):
            for word in document.split():
                self.inverted_index[word].append(docid)

    def calculate_cosine_similarity(self):
        return cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def print_cosine_similarity(self):
        cosine_similarities = self.calculate_cosine_similarity()
        print("Cosine Similarity Matrix:")
        print(cosine_similarities)

    def serialize(self, vectorizer_filename, matrix_filename):
        with open(vectorizer_filename, "wb") as vectorizer_file:
            pickle.dump(self.tfidf_vectorizer, vectorizer_file)
        with open(matrix_filename, "wb") as matrix_file:
            pickle.dump(self.tfidf_matrix, matrix_file)

    def deserialize(self, vectorizer_filename, matrix_filename):
        with open(vectorizer_filename, "rb") as vectorizer_file:
            self.tfidf_vectorizer = pickle.load(vectorizer_file)
        with open(matrix_filename, "rb") as matrix_file:
            self.tfidf_matrix = pickle.load(matrix_file)

    def print_tfidf_scores(self):
        terms = self.tfidf_vectorizer.get_feature_names_out()
        print("\nTF-IDF Scores:")
        for i, doc in enumerate(self.tfidf_matrix):
            print(f"Document {i+1}:")
            for j, term in enumerate(terms):
                tfidf_score = doc[0, j]
                if tfidf_score > 0:
                    print(f"   {term}: {tfidf_score}")


    def search(self, query):
        query_vector = self.tfidf_vectorizer.transform([query])
        query_words = query.split()
        relevant_docs = set()
        for word in query_words:
            relevant_docs.update(self.inverted_index.get(word, []))
        relevant_docs = list(relevant_docs)
        relevant_docs.sort()
        if not relevant_docs:
            print("No documents found")
            return
        print(f"Documents relevant to query '{query}':")
        for doc_id in relevant_docs:
            print(f"   Document {doc_id+1}")


documents = [
    "Polished postings are nice",
    "Dogs are nice",
    "Plat is mean",
    "Cat is something"
]

indexer_tfidf = InvertedIndex()
indexer_tfidf.fit_transform(documents)
indexer_tfidf.print_tfidf_scores()
indexer_tfidf.print_cosine_similarity()
indexer_tfidf.search("second document")

