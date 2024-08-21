from transformers import pipeline, AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F


model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


def preprocess_description(description):
    """Preprocess the user description for searching."""
    return description.strip().lower()


def get_embedding(text):
    """Generate an embedding for the text and normalize it."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    normalized_embedding = F.normalize(embedding, p=2, dim=1)
    return normalized_embedding



def calculate_similarity(embedding1, embedding2):
    """Calculate cosine similarity between two embeddings and normalize the result."""
    similarity = F.cosine_similarity(embedding1, embedding2)
    return similarity.item()
