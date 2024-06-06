curl -fsSL https://ollama.com/install.sh | sh

pip install -r requirements.txt

git clone https://github.com/Rohit-K814307/open_rag/tree/windows
cd open_rag
conda env create -f environment.yml
#ollama create email_model_llama2 -f ./email_model_llama2.txt 