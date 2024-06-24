from ollama import Client
from open_rag.utils.retrieval import Retriever
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def get_documents(query, csv_path, myemail, n_dataset=100, n_docs=2, n_neighbors=20, model_name="prajjwal1/bert-medium"):

    retriever = Retriever(model_name, csv_path, myemail, n_dataset)
    return retriever.select_top_docs(query, n_docs, n_neighbors)


def augment_query(query, documents):

    full_query = query + "\n\n\nHere are the email documents to base your email style, tone, etc. (DO NOT COPY) off of: "

    for doc in documents:
        full_query += " \n" + str(doc)

    return full_query


def generate_email(query, 
                   csv_path, 
                   myemail, 
                   n_dataset=100, 
                   n_docs=2, 
                   n_neighbors=20, 
                   model_name="prajjwal1/bert-medium", 
                   ollama_name="email_model_llama2:latest",
                   ollama_host="http://localhost:11434"):

    documents = get_documents(query, csv_path, myemail, n_dataset, n_docs, n_neighbors, model_name)
    query = augment_query(query, documents)

    client = Client(host=ollama_host)
    
    modelfile = '''
    FROM llama2:latest
    PARAMETER temperature 0.2
    SYSTEM You are an email assistant, you help with composing new email responses using the same format, word choice, tone, and writing style given emails I have sent before. Do not use the same names, locations, etc. - I just want you to use the writing style and word choices that I use.
    '''
    client.create(model=ollama_name[0:ollama_name.index(":")], modelfile=modelfile)

    response = client.chat(model=ollama_name, messages=[
        {
            'role':'user',
            'content':query
        }
    ])

    llm = Ollama(
        base_url="http://localhost:11434",
        model="email_model_llama2",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )

    

    return response['message']['content']