from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document


print("loading faiss embedding mdoels>>>")

# loading the data 

with open("text_1.txt" ,"r",encoding='utf-8') as f:
    full_text=f.read()

print(f"load text data {len(full_text)} characters")

# splitting the text smartly 
text_splitter  = RecursiveCharacterTextSplitter(
    chunk_size= 700,
    chunk_overlap= 100,
    separators=["\n\n", "\n", ".", "?", "!", "•", ":", "-"]
)
chunks = text_splitter.split_text(full_text)

# converting chunk into the documents format 

document = [Document(page_content=chunk) for chunk in chunks]
print(f"split the chunk te len of doc{len(document)} length ")


# makind embedding techniques 
embeding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# creating vector store using faiss
vectore_store = FAISS.from_documents(document,embeding)

# storing the vectore index into our pc

vectore_store.save_local("faiss_index_mumbai_data")
print("🎯 Vector database created and saved successfully as 'faiss_index_mumbai'")

# Test loading
try:
    test_store = FAISS.load_local("faiss_index_mumbai_data", embeding, allow_dangerous_deserialization=True)
    print("✅ Index loaded successfully - ready to use!")
except Exception as e:
    print(f"❌ Error loading index: {e}")
