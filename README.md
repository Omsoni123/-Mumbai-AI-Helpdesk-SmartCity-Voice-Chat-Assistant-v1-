# 🏙️ Mumbai AI Helpdesk – Voice & Chatbot Assistant

## 📑 Table of Contents

* [Overview](#-overview)
* [Real-World Impact](#-real-world-impact)
* [Features](#- Features OF this project )
* [Tech Stack](#-tech-stack)
* [Installation](#-installation)
* [Usage](#-usage)
* [How It Works](#-how-it-works)
* [API Endpoints](#-api-endpoints)
* [Future Improvements](#-future-improvements)
* [Author](#-author)
* [License](#-license)
* [Hashtags](#-hashtags)

## 🚀 Overview

The **Mumbai AI Helpdesk** is an intelligent voice-enabled and chat-based system designed to provide real-time information about Mumbai. It helps citizens and tourists access transportation details, emergency services, tourism info, and general city guidance.

## 🌱 Real-World Impact

This project helps citizens by:

* Providing instant voice-based answers.
* Making city information more accessible.
* Reducing dependency on manual helpdesks.
* Improving awareness about public services.
* Supporting tourists with accurate and fast information.

## 🌟 Features OF this project 

* 🎙️ **Voice Input Support** (Speech-to-Text)
* 🔊 **Text-to-Speech Output**
* 🤖 **AI-based conversational responses**
* 📚 **RAG (Retrieval-Augmented Generation) for accurate city data**
* ⚡ **Fast and lightweight**
* 🌐 **Web Interface + API Support**

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **AI/ML:** HuggingFace Transformers, LangChain, RAG pipeline
* **Speech Processing:** SpeechRecognition, pyttsx3
* **Vector DB:** FAISS
* **Deployment:** Docker (optional), GitHub Pages / Render / AWS

## 📌 Installation

```bash
# Clone repository
git clone https://github.com/Omsoni123/Mumbai-AI-Helpdesk.git
cd Mumbai-AI-Helpdesk

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
```

## 🖼️ Usage

1. Open the web app.
2. Click "🎤 Start Recording" to speak.
3. The AI listens, understands, and generates replies.
4. Or simply use the chat input box.

## 📊 How It Works

* Uses **ASR** to convert speech → text.
* The text query is processed by the **RAG model**.
* Response is generated using **LLM + Vector Store**.
* **TTS** speaks the response back to the user.

## 🔗 API Endpoints

| Method | Endpoint  | Description                                        |
| ------ | --------- | -------------------------------------------------- |
| `POST` | `/ask`    | Send a question and receive an AI-generated answer |
| `GET`  | `/health` | Check system health                                |

## 🚀 Future Improvements

* Add multi-language support (Hindi, Marathi)
* Deploy on cloud (AWS/GCP/Render)
* Add mobile app UI
* Add Mumbai map-based navigation system

## 👨‍💻 Author

**Om Soni**
📧 [om.soni2706@gmail.com](mailto:om.soni2706@gmail.com)
🔗 GitHub: github.com/Omsoni123
🔗 LinkedIn: linkedin.com/in/om-soni-8b0643231

## 📜 License

MIT License

## 🏷️ Hashtags

```
#AI #Chatbot #VoiceAssistant #Mumbai #SmartCity #RAG #Flask #Python #NLP
#SpeechToText #TextToSpeech #LangChain #HuggingFace #MachineLearning
#AIAssistant #CityHelpdesk #OpenSource #OmSoniProjects
```
## Example 
<img width="1879" height="469" alt="Screenshot 2025-11-06 203803" src="https://github.com/user-attachments/assets/7a447e02-bd21-4dca-a20e-d50fd960e612" />
<img width="1873" height="323" alt="Screenshot 2025-11-06 203541" src="https://github.com/user-attachments/assets/054b820a-fe79-454e-aaee-dc5e4cbd9ea4" />
<img width="1582" height="217" alt="Screenshot 2025-11-06 203921" src="https://github.com/user-attachments/assets/f7c7a07b-e744-424a-9ea8-70aa2f5ea0f0" />




