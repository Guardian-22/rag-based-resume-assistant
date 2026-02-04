# RAG-Based Resume Assistant

A Resume Question-Answering Assistant that uses Retrieval-Augmented Generation (RAG) with a local LLM to answer questions about resumes. Users can interact with their resume in a conversational manner and get insights or suggestions based strictly on the provided resume content.

This project is built using Python, LangChain, FAISS, Ollama, and Streamlit for the UI.

## Features

PDF Resume Loader: Load resumes in PDF format and convert them into manageable chunks.

Text Chunking: Splits long resumes into logical chunks for better retrieval.

FAISS Vector Store: Builds embeddings for the chunks and allows fast retrieval of relevant information.

RAG (Retrieval-Augmented Generation): Combines retrieved chunks with a local LLM for accurate responses.

Interactive Chat: Users can ask questions about their resume and get concise answers.

Streamlit UI: Clean, interactive interface for testing and exploring the assistant.

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/rag-based-resume-assistant.git
```
```bash
cd rag-based-resume-assistant
```
### Install dependencies with Poetry
```bash
poetry install
```

### Make sure Ollama is installed and models are available


### To Run :- 
```bash
poetry run streamlit run src/rag_based_resume_assistant/app.py
```
## Future Improvements

Support multiple resume formats (Word, TXT).

Add automatic summarization and improvement suggestions.

Add an option to upload a resume file directly via the Streamlit interface.

Integrate multiple resumes and allow comparison/analysis.

Deploy with Docker for easier sharing and reproducibility.
