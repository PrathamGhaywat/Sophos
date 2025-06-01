from model import get_kw, model_ans
from arxiv_bot import fetch_arxiv_articles
import streamlit as st

# Set page config
st.set_page_config(page_title="Sophos - Research Agent", layout="centered")

st.title("📚 Sophos - Your AI Research Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to handle research pipeline
def research(prompt):
    try:
        kw = get_kw(prompt)
        articles = fetch_arxiv_articles(kw)
        answer = model_ans(prompt, articles)
        return answer
    except Exception as e:
        return f"⚠️ Error: {e}"

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Show user prompt
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = research(prompt)
            st.markdown(response)

    # Save response to session
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style="text-align: center; color: gray;">
        <small>Built by Pratham Ghaywat: https://github.com/prathamghaywat</small>
    </div>
    """,
    unsafe_allow_html=True
)