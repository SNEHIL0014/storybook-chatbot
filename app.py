# ==========================================
# Storybook Chatbot (Limited Memory, LOCAL)
# Children's Story: Little Red Riding Hood
# Model: FLAN-T5 (Instruction-tuned, FREE)
# ==========================================

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ---------- Load Story ----------
def load_story(file_path="story.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

story_text = load_story()
print("Story loaded successfully.")
print("Story length:", len(story_text))

# ---------- Load Instruction Model ----------
print("Loading local instruction model (FLAN-T5)... Please wait.")

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
model.eval()

print("\nStoryBot is ready!")
print("Ask questions about the story. Type 'exit' to quit.\n")

# ---------- Limited Memory ----------
MEMORY_SIZE = 3
chat_memory = []

# ---------- Generate Response ----------
def generate_response(user_input):
    global chat_memory

    # ---------- Safety Filter (prevents hallucination) ----------
    forbidden_keywords = [
        "phone", "number", "mobile", "email", "instagram",
        "whatsapp", "address", "pin", "aadhaar", "contact"
    ]

    if any(word in user_input.lower() for word in forbidden_keywords):
        return "I can only answer questions that are part of the story."

    # ---------- Maintain Limited Memory ----------
    chat_memory.append(user_input)
    chat_memory = chat_memory[-MEMORY_SIZE:]

    # ---------- Prompt ----------
    prompt = f"""
You are a children's story assistant.

Answer ONLY using the story below.
Use simple, child-friendly language.

If the answer is not clearly mentioned in the story, say:
"I can only answer based on the story."

STORY:
{story_text}

QUESTION:
{user_input}

ANSWER:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=80,
            do_sample=False  # factual & stable
        )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # ---------- Final Safety Check ----------
    if not answer or len(answer.split()) < 2:
        return "I can only answer based on the story."

    return answer


# ---------- Chat Loop ----------
while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    if not user_input:
        continue

    reply = generate_response(user_input)
    print("Bot:", reply)
    print()  # spacing for readability
