# model.py
from transformers import pipeline

def load_model():
    # Use Hugging Face pipeline to load a text generation model
    generator = pipeline('text-generation', model='gpt2')
    return generator

def generate_text(prompt):
    model = load_model()
    result = model(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']
