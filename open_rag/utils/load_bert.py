from transformers import AutoModel, AutoTokenizer
import torch

class BERT():

    def __init__(self, model_name):
        """
        Arguments: 
        
        - model_name (srt): bert model to be used
        
        """

        self.model_name = model_name

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.bert = AutoModel.from_pretrained(model_name)
    

    def predict(self, text, max_length):
        """
        Arguments:

        - text (list or str): input to bert prediction
        
        """

        tokenized_ex = self.tokenizer(text,padding="max_length", truncation=True, return_tensors="pt", max_length=max_length)

        with torch.no_grad():
            output = self.bert(tokenized_ex["input_ids"], tokenized_ex["token_type_ids"], tokenized_ex["attention_mask"])["last_hidden_state"]

        squashed = []

        for i in range(len(output)):
            embedding = output[i]
            vector = []
            for x in range(len(embedding)):
                mean = torch.mean(embedding[x])
                vector.append(mean.item())
            squashed.append(vector)

        return torch.tensor(squashed) 