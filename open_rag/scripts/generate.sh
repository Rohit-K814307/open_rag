#!/bin/bash

#help function & setup inputs

helpFunction()
{
   echo ""
   echo "Usage: $0 -q {query string} -c {path to csv} -e {email address} -s {dataset size} -d {number of documents} -n {number of neighbors} -v {vector algorithm} -l {ollama llm}"
   echo -e "\t-q Input query to LLM"
   echo -e "\t-c CSV Path to Documents"
   echo -e "\t-e Email address (lowercase)"
   echo -e "\t-s Dataset Size"
   echo -e "\t-d Number of docs for LLM query augmentation"
   echo -e "\t-n Number of neighbors for nearest neighbors algorithm"
   echo -e "\t-v Name of vectorization model to use"
   echo -e "\t-l Name of ollama LLM to query"
   exit 1 
}

while getopts "q:c:e:s:d:n:v:l:" opt
do
   case "$opt" in
      q ) query="$OPTARG" ;;
      c ) csv="$OPTARG" ;;
      e ) email="$OPTARG" ;;
      s ) size="$OPTARG" ;;
      d ) num_docs="$OPTARG";;
      n ) num_neigh="$OPTARG";;
      v ) vect_alg="$OPTARG";;
      l ) ollama_llm="$OPTARG";;
      h ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$query" ] || [ -z "$csv" ] || [ -z "$email" ]
then
   echo "Some or all required parameters are empty";
   helpFunction
fi

if [ -z "$size" ] 
then
   size=100
fi

if [ -z "$num_docs" ] 
then
   num_docs=2
fi

if [ -z "$num_neigh" ] 
then
   num_neigh=20
fi

if [ -z "$vect_alg" ] 
then
   model_name="prajjwal1/bert-medium"
fi

if [ -z "$ollama_llm" ] 
then
   ollama_llm="email_model_llama2"
fi

echo "make sure to run ollama serve in your shell"
python -m open_rag.utils.generate_email "$query" "$csv" "$email" "$size" "$num_docs" "$num_neigh" "$model_name" "$ollama_llm"