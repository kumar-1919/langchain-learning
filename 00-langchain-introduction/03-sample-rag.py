from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

# 1. Load PDF
loader = PyPDFLoader("data/handbook.pdf")
docs = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. Create embeddings
embedding = OllamaEmbeddings(model="nomic-embed-text")

# 4. Store in vector DB
db = Chroma.from_documents(chunks, embedding=embedding, persist_directory="db")

# 5. Create Retriever
retriever = db.as_retriever()

# 6. Define LLM
llm = Ollama(model="llama3")

# 7. Create Retrieval QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 8. Ask a question
query = "What are the refund policies in the document?"
answer = qa_chain.run(query)
print(answer)
