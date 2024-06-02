import torch 
import numpy as np
from sklearn.neighbors import NearestNeighbors
from open_rag.utils.load_bert import BERT
from open_rag.data.read_data import DataSet


class Retriever():

    def __init__(self, model_name, csv_dir, myemail, n_dataset):

        self.model_name = model_name
        self.csv_dir = csv_dir


        self.dataset = DataSet(self.csv_dir, myemail, n_dataset)


        self.bert = BERT(self.model_name)

        self.documents = self.dataset.emails
        self.doc_max_length = len(max(self.documents, key = len))
        self.encoded_documents = self.get_document_encodings()


    def get_document_encodings(self):
        return self.bert.predict(self.documents, self.doc_max_length)


    def encode_query(self, query):
        return self.bert.predict(query, self.doc_max_length)


    def get_nearest_neighbors(self, query, docs, n=5):

        nn = NearestNeighbors(n_neighbors=len(docs))

        nn.fit(docs.numpy())

        neighbors = nn.kneighbors(query.numpy(), n, return_distance=False)

        doc_enc = [docs[i] for i in neighbors[0]]

        doc_nonenc = [self.documents[i] for i in neighbors[0]]

        return {"Doc": doc_nonenc,
                             "Encode": doc_enc
                            }
        

    def compare_query_document(self, query, doc):
        return torch.cosine_similarity(doc,query).item()


    def compare_query_documents(self, query, documents, encoded_documents):
        
        out = {}

        for i in range(len(encoded_documents)):

            out[self.compare_query_document(query, encoded_documents[i])] = documents[i]

        return out
    

    def select_top_docs(self, query, n_docs=2, n_neighbors=5):

        query = self.encode_query(query)

        neighbors = self.get_nearest_neighbors(query, self.encoded_documents, n=n_neighbors)

        doc_comp = neighbors["Encode"]
        doc_ind = neighbors["Doc"]

        query_docs = self.compare_query_documents(query, doc_ind, doc_comp)

        scores = list(query_docs.keys())

        top_ind = np.asarray(np.argpartition(scores, -n_docs)[-n_docs:])

        top_ind = top_ind[np.argsort(np.asarray(scores)[top_ind])]

        return [query_docs[i] for i in [scores[i] for i in top_ind]]