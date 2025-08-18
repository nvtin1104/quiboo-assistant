from .model import model, tokenizer
from .db import save_interaction, get_last_interactions
import torch

def build_prompt(user_input):
    rows = get_last_interactions()
    history_text = "\n".join([f"User: {u}\nAssistant: {a}" for u,a in rows])
    return f"{history_text}\nUser: {user_input}\nAssistant:"

def chat(user_input, max_new_tokens=200):
    prompt = build_prompt(user_input)
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).split("Assistant:")[-1].strip()
    save_interaction(user_input, answer)
    return answer
