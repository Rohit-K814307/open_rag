from flask import Flask, request, render_template
import pandas as pd
from open_rag.utils.generation import generate_email
from flask_ngrok2 import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        if not request.files.get("csvfromoutlook"):
            df = pd.read_csv("open_rag\\data\\NVTEI_base.csv")
        else:
            df = pd.read_csv(request.files.get("csvfromoutlook"))
        
        query = request.form["query"]
        email_id = request.form["emailclass"]

        #params
        if not request.form["ndataset"]:
            n_dataset = 30
        else:
            n_dataset = int(request.form["ndataset"])

        if not request.form["ndocs"]:
            n_docs = 3
        else:
            n_docs = int(request.form["ndocs"])
        
        if not request.form["nneighbors"]:
            n_neighbors = 10
        else:
            n_neighbors = int(request.form["nneighbors"])

        email = generate_email(query, df, email_id, n_dataset, n_docs, n_neighbors)


        return render_template('email.html', email=email)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run()