FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt ./

RUN apt-get update && apt-get install git -y

RUN curl - fsSL https://ollama.com/install.sh | sh

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./open_rag ./open_rag

COPY ./open_rag_api ./open_rag_api

COPY ./__init__.py ./__init__.py

COPY ./email_model_llama2.txt ./email_model_llama2.txt

EXPOSE 5001

CMD ["python", "-m", "open_rag_api.app"]