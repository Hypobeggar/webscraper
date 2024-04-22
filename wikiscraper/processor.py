from flask import Flask, request, jsonify


app = Flask(__name__)


sample_data = [
    {'id': 1, 'title': 'The Fair', 'description': 'A fair'},
    {'id': 2, 'title': 'The Affair', 'description': 'An affair'},
    {'id': 3, 'title': 'The Stairs', 'description': 'The stairs'}
]

def process_query(query_text, top_k=3):
    if not query_text:
        return {'error': 'Query is empty or missing'}

    ranked_results = sorted(sample_data, key=lambda x: len(x['description']), reverse=True)[:top_k]
    return {'results': ranked_results}

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
