curl -fsSL https://ollama.com/install.sh | sh

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh


git clone https://github.com/Rohit-K814307/open_rag/tree/windows
cd open_rag
conda env create -f environment.yml
ollama create email_model_llama2 -f ./email_model_llama2.txt 