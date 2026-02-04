import streamlit as st
from orchestrator import ResumeAssistant

# Initialize the assistant
PATH="src/rag_based_resume_assistant/data/Kshitij-Lalge-AIML.pdf"
assistant = ResumeAssistant(PATH)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": assistant.system_prompt}]

st.title("Resume Chat Assistant 💼")
user_input = st.text_input("Ask a question about the resume:")

if user_input:
    reply, st.session_state.messages = assistant.ask(user_input, st.session_state.messages)
    st.write(reply)

# show conversation history
st.sidebar.header("Conversation History")
for msg in st.session_state.messages:
    st.sidebar.write(f"{msg['role']}: {msg['content']}")
