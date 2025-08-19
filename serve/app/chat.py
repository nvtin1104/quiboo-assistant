import torch
from .model import model, tokenizer

def chat(user_input: str, max_new_tokens: int = 200) -> str:
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
