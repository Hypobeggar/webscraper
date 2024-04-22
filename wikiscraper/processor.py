from flask import Flask, request, jsonify
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)


sample_data = [
    {'id': 1, 'title': 'The Fair', 'description': 'A fair'},
    {'id': 2, 'title': 'The Affair', 'description': 'An affair'},
    {'id': 3, 'title': 'The Stairs', 'description': 'The stairs'}
]

def process_query(text, top_k=3):
    if not text:
        return {'error': 'Query is empty or missing'}

    
    descriptions = [data['description'] for data in sample_data]

   
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text] + descriptions)


    vector = tfidf_matrix[0]
    description_vectors = tfidf_matrix[1:]
    similarities = cosine_similarity(vector, description_vectors)


    index = np.argsort(similarities[0])[::-1][:top_k]
    results = [sample_data[i] for i in index]

    return {'results': results}

@app.route('/query', methods=['POST']) # AiAgent ChatGPT
def handle_query():

    data = request.json
    
    if 'query' in data:

        query_text = data['query']
        response = process_query(query_text)
        return jsonify(response)
    else:

        error_response = {'error': 'Missing query in JSON data'}
        return jsonify(error_response), 400


if __name__ == '__main__':
    app.run(debug=True)
