import os
import streamlit as st
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

st.set_page_config(
    page_title="Maha Bank Loan Product Assistant",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank of Maharashtra Loan Product Assistant")
st.markdown(
    "💬 Ask me anything about **Bank of Maharashtra loan products** — "
    "eligibility, interest rates, charges, or schemes."
)

## Side bar
st.sidebar.header("⚙️ LLM Settings")

model_choice = st.sidebar.selectbox(
    "Choose Model:",
    ["gpt-4.1-nano", "gpt-4o-mini", "gpt-3.5-turbo"]
)

temperature = st.sidebar.slider(
    "Creativity (Temperature):", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.7, 
    step=0.1, 
    format="%.2f"
)


max_tokens = st.sidebar.selectbox(
    "Max Tokens:", [256, 512, 1024], index=1
)

# API Setup
EURI_API_KEY = (
    st.secrets["api_keys"]["EURI_API_KEY"]
    if "api_keys" in st.secrets and "EURI_API_KEY" in st.secrets["api_keys"]
    else os.getenv("EURI_API_KEY")
)

EURI_BASE_URL = (
    st.secrets["api_keys"]["EURI_BASE_URL"]
    if "api_keys" in st.secrets and "EURI_BASE_URL" in st.secrets["api_keys"]
    else os.getenv("EURI_BASE_URL", "https://api.euron.one/api/v1/euri")
)

# Ensure keys exist
if not EURI_API_KEY:
    raise ValueError("❌ EURI_API_KEY is missing. Set it in .env or Streamlit secrets.")

# Set OpenAI-compatible env variables
os.environ["OPENAI_API_KEY"] = EURI_API_KEY
os.environ["OPENAI_BASE_URL"] = EURI_BASE_URL

# LLM
llm = ChatOpenAI(
    model=model_choice,
    temperature=temperature,
    max_tokens=max_tokens
)

# Embeddings + FAISS
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
vectorstore = FAISS.load_local(
    "faiss_index_bom",
    embedding_model,
    index_name="index", 
    allow_dangerous_deserialization=True
    )

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4})
)

# User Input
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #1E90FF;  /* Dodger Blue */
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #0b63c9;  /* Darker blue on hover */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.subheader("🔍 Ask to your Assistant")

user_question = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_question.strip():
        with st.spinner("🤔 Thinking..."):
            answer = qa_chain.run(user_question)
        st.success("✅ Answer Generated!")
        st.markdown("### 📌 Answer")
        st.info(answer)
    else:
        st.warning("⚠️ Please enter a valid question.")
        
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>"
    "🚀 NexusAI powered by <b>Omkar Bhosale</b>"
    "</div>",
    unsafe_allow_html=True
)
