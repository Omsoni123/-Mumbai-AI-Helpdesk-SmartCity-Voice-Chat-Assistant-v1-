# 🏙️ SmartCity Mumbai Helpdesk – AI Voice Assistant 💬🎙️

“An intelligent AI-powered helpdesk that brings Mumbai City information to life — through voice and chat.”
— Developed with ❤️ by Om Soni

✨ About the Project

SmartCity Mumbai Helpdesk is a voice-enabled chatbot designed to provide instant answers about Mumbai — from transportation and healthcare to education, tourism, and government services.
It’s built using Flask, LangChain, FAISS, and Hugging Face models, with both Text-to-Speech (TTS) and Speech Recognition (ASR) support.

This project is a blend of AI + Web + Voice — turning raw city data into a conversational experience.

🚀 Features

✅ Interactive Voice & Chat Interface – Speak or type your questions
✅ Smart Search using FAISS Vector DB – Accurate and context-aware answers
✅ Local LLM (Flan-T5) – Fast, offline-friendly responses
✅ Dynamic UI – Sleek, dark-themed chat interface with animations
✅ Text-to-Speech (pyttsx3) – Bot replies in a natural voice
✅ Speech Recognition (Web Speech API) – Hands-free interaction
✅ Built with LangChain + HuggingFace – Reliable NLP stack
✅ Modular Flask Architecture – Scalable and easy to extend

🧩 Tech Stack
Category	Technology
💻 Backend	Flask, Python
🧠 AI / NLP	LangChain, Hugging Face, Flan-T5
🔍 Vector DB	FAISS (Sentence Transformers Embeddings)
🗣️ Voice	pyttsx3 (TTS) + Web Speech API (ASR)
💅 Frontend	HTML, CSS, JavaScript
⚙️ Model	google/flan-t5-base
🧱 Data Source	Mumbai City Dataset (Custom curated)


🗂️ Project Structure
smartcity_mumbai_helpdesk/
│
├── templates/
│   └── index.html        # Main chat interface (UI)
│
├── static/
│   ├── style.css         # Modern dark theme styling
│   └── script.js         # Frontend logic (ASR + TTS)
│
├── faiss_index_mumbai/   # FAISS index folder (vector store)
│
└── app.py                # Flask + LangChain


🧠 Example Questions to Ask
🏥 Hospitals
“Government hospitals in Mumbai?”
“Where is KEM Hospital located?”
“Best hospital near Andheri?”

🚉 Transportatio
“How to reach Bandra from CST?”
“When do Mumbai local trains start?”
“Metro stations near Ghatkopar?”

🎓 Education
“Top colleges in Mumbai.”
“Best engineering colleges near Andheri.”
“Where is IIT Bombay located?”

🌇 Tourism
“Tourist places in South Mumbai.”
“What is famous in Bandra?”
“Tell me about Gateway of India.”

🏛️ Government
“Who is the Chief Minister of Maharashtra?”
“Where is Mantralaya located?”

🚨 Emergency
“Ambulance number in Mumbai.”
“Fire brigade helpline.”

🌟 Future Enhancements

⌛ Typing dots animation
🔁 Conversation memory
🌗 Light/Dark mode toggle
☁️ Deployment on Render / AWS
📊 Analytics dashboard

🧑‍💻 Developer
👤 Om Soni
AI & Data Science enthusiast | Backend + ML Developer

⭐ If you like this project, please star the repo on GitHub!

🏁 Final Note
“SmartCity Mumbai Helpdesk – making city information simple, interactive, and voice-powered.”
