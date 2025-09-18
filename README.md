# Bank-of-Maharashtra-Loan-Product-Assistant-using-RAG

AI-powered Loan Product Assistant for **Bank of Maharashtra** using Retrieval-Augmented Generation (RAG).  
The system scrapes official BOM loan product pages, cleans and processes the data, builds a **FAISS index with sentence-transformer embeddings**, and answers user queries on **interest rates, tenure, eligibility, and concessions** through a **Streamlit app**.

---

## 📂 Project Directory (as per local setup)

```

Bank-of-Maharashtra-Loan-Product-Assistant-using-RAG/
├── .env                         # Environment variables (NOT committed)
├── .ipynb\_checkpoints/          # Jupyter checkpoints
├── .streamlit/                  # Streamlit config (secrets.toml excluded)
├── app.py                       # Streamlit chatbot application
├── BOM Product Assistant RAG.ipynb  # Jupyter notebook (scraping + pipeline)
├── bom\_data/                    # Cleaned scraped loan text files
├── chroma\_db/                   # Optional Chroma vector index
├── faiss\_index\_bom/             # FAISS vector index (generated locally)
├── requirements.txt             # Python dependencies

````

---

## 🚀 Project Setup

### 1. Clone Repository
```bash
git clone https://github.com/omkarbhosale1623/Bank-of-Maharashtra-Loan-Product-Assistant-using-RAG.git
cd Bank-of-Maharashtra-Loan-Product-Assistant-using-RAG
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` → `.env` and add your keys:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.euron.one/api/v1/euri
```

### 4. Run Jupyter Notebook

Execute the pipeline to scrape, clean, chunk, and build FAISS index:

```bash
jupyter notebook "BOM Product Assistant RAG.ipynb"
```

### 5. Launch Streamlit App

```bash
streamlit run app.py
```

---

## 🏗️ Architectural Decisions

### 📚 Libraries

* **BeautifulSoup4 + Requests** → Scraping loan pages
* **LangChain** → Document loading, chunking, embeddings, RAG orchestration
* **FAISS** → Lightweight vector database for semantic search
* **Sentence-Transformers (all-mpnet-base-v2)** → Embedding model for retrieval
* **ChatOpenAI (via Euri API)** → LLM for generating answers
* **Streamlit** → UI for interactive queries
* **dotenv** → Safe API key management

### 📊 Data Strategy

* Focused scraping of official BOM loan product pages only
* Regex cleaning to remove footers, disclaimers, social links
* **RecursiveCharacterTextSplitter** → 300-character chunks with 50 overlap for optimal retrieval

### 🤖 Model Selection

* **Embeddings**: `all-mpnet-base-v2` → strong semantic similarity
* **LLM**: `gpt-4.1-nano` (Euri API) → efficient + cost-friendly

---

## 🚧 Challenges Faced

* **Inconsistent Page Formats** → handled with regex + keyword filtering
* **Dynamic/Verbose HTML** → stripped nav/ads/disclaimers before indexing
* **Context Limits** → solved via recursive chunking strategy
* **API Key Security** → handled with `.env` + `.gitignore`

---

## 🔮 Potential Improvements

* Hybrid search (semantic + keyword)
* Dockerization for deployment
* Session memory in Streamlit app
* Move to production vector DB (Pinecone/Weaviate)
* Add monitoring for loan product updates

---

## 🧪 Testing

Inside the notebook or Streamlit app, try questions like:

* *“What are the interest rates for a Bank of Maharashtra home loan?”*
* *“What is the maximum tenure for a personal loan if my salary account is with the bank?”*
* *“Tell me about the Maha Super Flexi Housing Loan Scheme.”*
* *“Are there any processing fee concessions for women or defence personnel on home loans?”*

---

## 🤝 Contributing

1. Fork the repo
2. Create feature branch:

   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit changes:

   ```bash
   git commit -m "Add feature"
   ```
4. Push to branch:

   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request

---

## 📝 License

This project is under the **MIT License**.
⚠️ For **educational/demonstration use only**. Please respect **Bank of Maharashtra’s terms of service** when scraping their site.

