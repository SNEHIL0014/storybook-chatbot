Magic Storybook AI: Little Red Riding Hood
Developed for Children's Interactive Literacy
This project is a specialized AI chatbot designed to interact with children based on the story of Little Red Riding Hood. It utilizes Limited Memory Generative AI to provide accurate, safe, and context-aware responses while operating entirely on free, open-source models.

---
Task Requirements & Implementation

## 🎯 Task Requirements & Implementation

| Requirement | Implementation Strategy |
| :--- | :--- |
| **Limited Memory AI** | Utilizes a **Conversational Buffer** (sliding window) to maintain context (like follow-up questions) without exceeding memory limits. |
| **AI Engine & Model** | Built with **Hugging Face Transformers** using **Google FLAN-T5-Base** for high reasoning efficiency on standard hardware. |
| **AI Version** | **100% Free/Open Source.** Runs locally using `torch` and `transformers`; no paid API keys required. |
| **Story Content** | Grounded strictly in `story.txt` to eliminate hallucinations and ensure factual accuracy. |

---
🛡️ Kid-Friendly & Safety Features
Safety is the core priority of this "Magic Storybook" application. I have implemented three layers of protection:

Domain Guarding (The "Sweet Refusal"): The bot includes a semantic filter that blocks off-topic queries. If a child asks about modern technology, internet searches, or superheroes like "Batman," the bot provides a gentle, thematic redirection back to the story world.

Accuracy Grounding: By injecting the full text of the story into the model's prompt for every query, I have eliminated "hallucinations." The bot only answers based on the facts provided in the text.

Humanized Persona: The AI is tuned with a low temperature (0.1) setting. This ensures responses remain calm, factual, and predictable—perfect for a children's environment.

---
🏗️ Technical Architecture
Front-End: Gradio web interface for a clean, accessible, and responsive user experience.

Back-End: Python-based logic handling the grounding and safety filters.

Version Control: Professional repository structure including a .gitignore to exclude large environment files, ensuring a lightweight and clean repo.

---
How to Run

Install Dependencies:
pip install gradio torch transformers sentencepiece

Execute Application:
python app.py

Access UI: Open http://127.0.0.1:7861 in your browser.

---
🧪 Suggested Testing Sequence
To verify the system's performance and accuracy:

Factual: "What was in the basket?" (Tests Retrieval Accuracy)

Follow-up: "Who gave it to her?" (Tests Limited Memory Context)

Safety: "Can Batman help her?" (Tests Domain Guarding/Kid-Friendly Filter)

Abstract: "What is the moral of the story?" (Tests Thematic Logic)

---


