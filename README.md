# 🎙️ AI Voice Bot (Enterprise Edition)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/GPT--5.6-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![Whisper](https://img.shields.io/badge/Faster--Whisper-black?style=for-the-badge&logo=openai)](https://github.com/SYSTRAN/faster-whisper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An advanced, end-to-end Voice AI Agent designed for intelligent contact centers. This project integrates cutting-edge STT, LLM, and TTS technologies to provide a seamless, human-like conversational experience for customer support automation.

---

## ✨ Key Features

- **Real-time STT:** Powered by `Faster-Whisper` (Large-v3/Small) for high-accuracy Persian speech recognition.
- **Intelligence Layer:** Integrated with **GPT-5** for complex intent recognition and sentiment analysis.
- **Neural TTS:** Natural-sounding Persian voice synthesis using `Edge-TTS` (Dilara Neural).
- **Enterprise UI:** A modern, Dark-themed dashboard with Glassmorphism design, featuring:
  - Live Waveform Visualizer.
  - Real-time Latency & Confidence metrics.
  - System Operation Logs.
- **Bare-metal Ready:** Optimized for Ubuntu 24.04 LTS and HP ProLiant environments.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python 3.10+, FastAPI | High-performance asynchronous API framework |
| **Speech-to-Text** | Faster-Whisper (CTranslate2) | Optimized Whisper engine for fast transcription |
| **Brain (LLM)** | GPT-5.6 via OpenAI API | Persian intent processing and logical reasoning |
| **Text-to-Speech** | Microsoft Edge TTS | High-fidelity Persian voice synthesis |
| **Frontend** | HTML5, CSS3, Vanilla JS | Interactive Glassmorphism UI with real-time logging |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher.
- NVIDIA GPU with CUDA support (Recommended for low-latency production setups) or CPU.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aref-Shahsavari/Voice-bot.git
   cd Voice-bot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate

   # On Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the application:**
   - **Using Python directly:**
     ```bash
     python app.py
     ```
   - **On Windows:** Double-click the `run.bat` file.

6. **Access the application:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

---

## 📊 Performance Monitoring
The system includes a built-in **Analytics Sidebar** to track:
- **Latency:** Total round-trip time from audio input to voice output.
- **Confidence:** STT transcription probability score.
- **Model Status:** Active LLM version tracking.

---

## 🏗️ Future Roadmap
- [ ] Multi-channel support (VoIP/SIP Integration).
- [ ] Integration with CRM databases for personalized responses.
- [ ] Real-time sentiment analysis dashboard.
- [ ] Fine-tuning Whisper for specific Persian accents.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

**Developed for AI Infrastructure Roadmap.**

=======
