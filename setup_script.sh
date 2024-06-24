sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.12-venv

python3 -m venv open_rag_env
cd open_rag_env/bin
source activate
cd ~/open_rag
pip install -r requirements.txt

curl -fsSL https://ollama.com/install.sh | sh
ollama create email_model_llama2 -f email_model_llama2.txt

python3 -m open_rag_api.app