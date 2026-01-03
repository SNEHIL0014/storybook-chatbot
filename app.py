import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_story():
    try:
        with open("story.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return "Little Red Riding Hood lived near a forest. Her grandmother gave her a red hood."

STORY_DATA = load_story()

MODEL_ID = "google/flan-t5-base" 
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)

def magic_storyteller(message, history):
    off_topic = ["batman", "phone", "gps", "internet", "google", "superman", "address", "email"]
    if any(word in message.lower() for word in off_topic):
        return "Oh, that sounds like a different adventure! 🌟 My magic book only knows about the forest, the grandmother, and the girl in red. Let's talk about them!"

    if any(word in message.lower() for word in ["moral", "lesson", "learn"]):
        return "The story teaches us to listen to our parents and stay on the safe path to stay out of trouble! ✨"

    prompt = f"Using the story provided, answer the question for a child. \nStory: {STORY_DATA}\nQuestion: {message}\nAnswer:"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.1)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "huntsman" in answer.lower() or "hunter" in answer.lower() or "saved" in message.lower():
        return "A brave huntsman heard the wolf and rescued Little Red Riding Hood and her grandmother! 🪓"
    
    if len(answer.split()) < 2 and answer.lower() != "red":
        return f"The story says it was {answer}."

    return answer

with gr.Blocks(title="StoryBot") as demo:
    gr.Markdown("""
    # 📖 The Magic Storybook Friend
    Welcome! I am an AI trained specifically on the story of **Little Red Riding Hood**. 
    I stay strictly on the path and never tell tales outside of my book!
    """)
    
    chatbot = gr.ChatInterface(
        fn=magic_storyteller,
        examples=[
            "Who gave her the red hood?", 
            "What was in the basket?", 
            "What did the mother warn her?",
            "Who saved the day?",
            "What is the moral of the story?"
        ],
        cache_examples=False
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), share=True)