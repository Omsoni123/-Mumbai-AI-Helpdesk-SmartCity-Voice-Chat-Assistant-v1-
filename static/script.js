document.addEventListener("DOMContentLoaded", () => {
  const queryInput = document.getElementById("query");
  const chatBox = document.getElementById("chatBox");
  const voiceBtn = document.getElementById("voiceBtn");
  const sendBtn = document.getElementById("sendBtn");

  // Append message bubbles
  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  // Bot typewriter effect
  async function typeWriter(text) {
    const msg = document.createElement("div");
    msg.classList.add("message", "bot");
    chatBox.appendChild(msg);
    for (let i = 0; i < text.length; i++) {
      msg.textContent = text.substring(0, i + 1);
      await new Promise(r => setTimeout(r, 10));
    }
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  // Send user query to Flask backend
  async function sendQuery() {
    const userQuery = queryInput.value.trim();
    if (!userQuery) return;

    appendMessage("user", userQuery);
    queryInput.value = "";
    appendMessage("bot", "🤔 Thinking...");

    try {
      const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userQuery })
      });

      const data = await res.json();
      chatBox.removeChild(chatBox.lastChild);
      await typeWriter(data.answer);

      // TTS (Text-to-Speech)
      if ("speechSynthesis" in window && data.answer) {
        const utter = new SpeechSynthesisUtterance(data.answer);
        utter.lang = "en-IN";
        utter.rate = 1;
        utter.pitch = 1;
        speechSynthesis.speak(utter);
      }
    } catch (err) {
      chatBox.removeChild(chatBox.lastChild);
      appendMessage("bot", "⚠️ Error connecting to backend.");
    }
  }

  sendBtn.addEventListener("click", sendQuery);
  queryInput.addEventListener("keypress", e => { if (e.key === "Enter") sendQuery(); });

  // 🎙️ Voice Recognition (ASR)
  voiceBtn.addEventListener("click", () => {
    if (!("webkitSpeechRecognition" in window)) {
      alert("🎤 Voice recognition not supported in this browser.");
      return;
    }
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.start();
    voiceBtn.textContent = "🎧 Listening...";
    voiceBtn.style.backgroundColor = "#16a34a";

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      queryInput.value = transcript;
      voiceBtn.textContent = "🎙️";
      voiceBtn.style.backgroundColor = "#58a6ff";
      sendQuery();
    };

    recognition.onerror = () => {
      voiceBtn.textContent = "🎙️";
      voiceBtn.style.backgroundColor = "#58a6ff";
      alert("⚠️ Could not capture voice, please try again.");
    };
  });
});
