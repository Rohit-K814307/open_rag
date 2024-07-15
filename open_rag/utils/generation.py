from langchain_community.llms import Ollama
from open_rag.utils.retrieval import Retriever


def get_documents(query, csv_path, myemail, n_dataset=100, n_docs=2, n_neighbors=20, model_name="prajjwal1/bert-medium"):

    retriever = Retriever(model_name, csv_path, myemail, n_dataset)
    return retriever.select_top_docs(query, n_docs, n_neighbors)


def augment_query(query, documents):

    full_query = query + "\n\n\nHere are the email documents to base your email style, tone, etc. (DO NOT COPY) off of: "

    for doc in documents:
        full_query += "NEW EMAIL BEGINNING NOW:\n" + str(doc)

    return full_query


def generate_email(query, 
                   csv_path, 
                   myemail, 
                   n_dataset=100, 
                   n_docs=2, 
                   n_neighbors=20, 
                   model_name="prajjwal1/bert-medium", 
                   ollama_name="email_model_llama2"):

    documents = get_documents(query, csv_path, myemail, n_dataset, n_docs, n_neighbors, model_name)
    query = augment_query(query, documents)

    llm = Ollama(model=ollama_name)
    resp = llm.invoke(query)
    return resp
    