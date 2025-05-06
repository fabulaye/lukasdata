from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model and tokenizer



model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)