from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS

class ResumeAssistant:
    SYSTEM_PROMPT = (
        """You are an AI assistant that answers questions strictly based on the provided resume context.
           If information is not present, say so."""
    )
    def __init__(self, pdf_path: str):
        self.loader = PyPDFLoader(pdf_path)
        self.docs = self.loader.load()

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        self.chunks = self.text_splitter.split_documents(self.docs)

        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.vectorstore = FAISS.from_documents(self.chunks, self.embeddings)
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})

        self.llm = ChatOllama(model="llama3.1:8b", temperature=0)
        self.system_prompt = self.SYSTEM_PROMPT
    
    def ask(self, question: str, messages=None):
        # Initialize messages if None
        if messages is None:
            messages = [{"role": "system", "content": self.system_prompt}]

        # Retrieve relevant chunks
        retrieved_docs = self.retriever.invoke(question)
        resume_context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        messages.append({"role": "system", "content": f"Relevant resume context:\n{resume_context}"})
        messages.append({"role": "user", "content": question})

        # Stream LLM response
        response_stream = self.llm.stream(messages)
        assistant_reply = ""
        for chunk in response_stream:
            assistant_reply += chunk.content

        messages.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply, messages
