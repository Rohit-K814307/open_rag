import sys
from open_rag.utils.generation import generate_email

query = str(sys.argv[1])
csv_path = str(sys.argv[2])
email = str(sys.argv[3])
n_dataset = int(sys.argv[4])
n_docs = int(sys.argv[5])
n_neighbors = int(sys.argv[6])
model_name = str(sys.argv[7])
ollama_name = str(sys.argv[8])


print(generate_email(query, csv_path, email, n_dataset, n_docs, n_neighbors, model_name, ollama_name))