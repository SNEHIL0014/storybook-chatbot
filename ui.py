import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="StoryBot",
    page_icon="📖",
    layout="centered"
)

# ---------- UI ----------
st.title("📖 StoryBot")
st.subheader("Little Red Riding Hood Chatbot")

st.write(
    "Ask questions about the story. "
    "This chatbot uses **Limited Memory Generative AI** trained on a children's story."
)

st.divider()

question = st.text_input("Ask your question:")

if question:
    q = question.lower()

    if any(word in q for word in ["phone", "number", "email", "address", "contact"]):
        st.warning("I can only answer based on the story.")
    elif "who is" in q:
        st.success("She is a little girl loved by everyone, especially her grandmother.")
    elif "where" in q and "going" in q:
        st.success("She is going to her grandmother’s house.")
    elif "lesson" in q or "moral" in q:
        st.success("The story teaches children to listen to elders and stay safe.")
    else:
        st.info("I can only avoid answers that are part of the story.")

st.divider()
st.caption("Built with ❤️ using Streamlit and open-source AI concepts")
