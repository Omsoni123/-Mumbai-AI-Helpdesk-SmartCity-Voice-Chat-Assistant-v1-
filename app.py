from flask import Flask, render_template, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
import torch
import pyttsx3
import os
import threading
import queue
import time

# ------------------------------------------------------
# ⚙️ Flask App Setup
# ------------------------------------------------------
app = Flask(__name__)

# ------------------------------------------------------
# ⚙️ Smarter Text-to-Speech Engine (Thread-Safe + Queued)
# ------------------------------------------------------
class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1)
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        else:
            self.engine.setProperty('voice', voices[0].id)

        # Thread-safe speech queue
        self.queue = queue.Queue()
        self.running = True
        threading.Thread(target=self._process_queue, daemon=True).start()

    def _process_queue(self):
        """Continuously process speech requests."""
        while self.running:
            text = self.queue.get()
            if text is None:
                break
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print("❌ TTS Error:", e)

    def speak_text(self, text):
        """Safely add text to queue for speaking."""
        if text.strip():
            self.queue.put(text)

# Initialize global TTS engine
tts_engine = TTSEngine()

def speak_text(text):
    """Public function for convenience."""
    tts_engine.speak_text(text)

# ------------------------------------------------------
# 🎤 Welcome Message (Async)
# ------------------------------------------------------
def play_welcome_message():
    """Plays welcome message after server starts."""
    time.sleep(2)
    welcome_text = "Welcome to Smart City Mumbai Help Desk. Developed by Mr. Om Soni. and khushi "
    print("🎉 Playing welcome message...")
    speak_text(welcome_text)

# ------------------------------------------------------
# ⚙️ Load FAISS Index and Model
# ------------------------------------------------------
print("🔹 Loading FAISS index and embeddings...")

if not os.path.exists("faiss_index_mumbai_data"):
    print("❌ FAISS index not found! Run create_faiss_fixed.py first.")
    exit(1)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

try:
    vectorstore = FAISS.load_local("faiss_index_mumbai_data", embeddings, allow_dangerous_deserialization=True)
    print("✅ FAISS index loaded successfully!")
except Exception as e:
    print(f"❌ Error loading FAISS: {e}")
    exit(1)

# ------------------------------------------------------
# ⚙️ Load Local LLM (FLAN-T5)
# ------------------------------------------------------
print("🔹 Loading model...")
device = 0 if torch.cuda.is_available() else -1
print(f"🧠 Using {'GPU' if device == 0 else 'CPU'}")

model_name = "google/flan-t5-base"
pipe = pipeline(
    "text2text-generation",
    model=model_name,
    max_new_tokens=100,
    temperature=0.3,
    device=device,
    repetition_penalty=1.1
)

llm = HuggingFacePipeline(pipeline=pipe)

# ------------------------------------------------------
# ⚙️ Prompt Template & QA Chain
# ------------------------------------------------------
prompt_template = """You are SmartCity Mumbai Helpdesk. Use the context below to answer briefly and helpfully.

Context: {context}

Question: {question}

Provide a clear, concise, and helpful answer in 2-3 lines maximum."""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=False,
    chain_type_kwargs={"prompt": prompt}
)

# ------------------------------------------------------
# 🌐 Flask Routes
# ------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("query", "").strip()
    if not user_input:
        return jsonify({"answer": "Please enter a question."})

    print(f"\n🧠 User asked: {user_input}")

    try:
        answer = qa_chain.run(user_input)
        print("🤖 Bot:", answer)

        # 🔊 Speak asynchronously (no overlap)
        speak_text(answer)

        return jsonify({"answer": answer})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"answer": "Sorry, something went wrong while generating the response."})

@app.route("/welcome", methods=["GET"])
def welcome():
    speak_text("Welcome to Smart City Mumbai Help Desk.")
    return jsonify({"status": "Welcome message played"})

# ------------------------------------------------------
# 🚀 Run Flask App
# ------------------------------------------------------
if __name__ == "__main__":
    print("🚀 SmartCity Helpdesk running at http://127.0.0.1:5000")
    print("🔊 TTS Engine active and thread-safe")
    print("💡 Voice-enabled chat ready for questions...")

    # Start welcome message thread
    threading.Thread(target=play_welcome_message, daemon=True).start()

    app.run(debug=True, host="0.0.0.0", port=5000)
