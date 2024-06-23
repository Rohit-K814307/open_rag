ollama serve
sleep 5
ollama create email_model_llama2 -f ./email_model_llama2.txt
tail -f /dev/null