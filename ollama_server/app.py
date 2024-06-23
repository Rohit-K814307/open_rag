from flask import Flask, jsonify
from open_rag.utils.generation import generate_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate(query, df, email_id, n_dataset, n_docs, n_neighbors):
    
    return jsonify({"email":generate_email(query, df, email_id, n_dataset, n_docs, n_neighbors)})
