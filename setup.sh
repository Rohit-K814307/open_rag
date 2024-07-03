pip install -r requirements.txt

curl -fsSL https://ollama.com/install.sh | sh

ollama serve & ollama create email_model_llama2 -f email_model_llama2.txt && python3 -m open_rag_api.app