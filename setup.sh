ollama serve & curl -fsSL https://ollama.com/install.sh | sh && pip install -r requirements.txt && ollama create email_model_llama2 -f email_model_llama2.txt && python3 -m open_rag_api.app