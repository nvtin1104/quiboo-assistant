import gradio as gr
from .chat import chat

def chat_fn(user_input):
    return chat(user_input)

demo = gr.Interface(fn=chat_fn, inputs="text", outputs="text", title="Trợ lý cá nhân AI")
demo.launch()
