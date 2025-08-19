from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

MODEL_ID = "facebook/blenderbot-400M-distill"
SAVE_PATH = "./models/blenderbot-400M-distill"

print("🔽 Đang tải model và tokenizer...")
tokenizer = BlenderbotTokenizer.from_pretrained(MODEL_ID)
model = BlenderbotForConditionalGeneration.from_pretrained(MODEL_ID)

tokenizer.save_pretrained(SAVE_PATH)
model.save_pretrained(SAVE_PATH)

print(f"✅ Model đã được lưu tại {SAVE_PATH}")
