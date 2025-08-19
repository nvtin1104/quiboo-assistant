from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "vinai/PhoGPT-4B-Chat"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
    torch_dtype="auto",
    device_map="auto"
)
