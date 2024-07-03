from flask import Flask, request, render_template
import pandas as pd
from open_rag.utils.generation import generate_email
from flask_ngrok2 import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        print("dog")

        df = pd.read_csv(request.files.get('file'))
        query = request.form["query"]
        email_id = request.form["emailid"]
        n_dataset = int(request.form["ndataset"])
        n_docs = int(request.form["ndocs"])
        n_neighbors = int(request.form["nneighbors"])

        print("dog")
        #email = generate_email(query, df, email_id, n_dataset, n_docs, n_neighbors)



        return render_template('email.html', email="dog")
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run()