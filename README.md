# 🎙️ Asiatech AI Voice Bot (Enterprise Edition)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/GPT--5.6-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![Whisper](https://img.shields.io/badge/Faster--Whisper-black?style=for-the-badge&logo=openai)](https://github.com/SYSTRAN/faster-whisper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An advanced, end-to-end Voice AI Agent designed for intelligent contact centers. This project integrates cutting-edge STT, LLM, and TTS technologies to provide a seamless, human-like conversational experience for **Asiatech** customer support automation.

---

## ✨ Key Features

-   **Real-time STT:** Powered by `Faster-Whisper` (Large-v3/Small) for high-accuracy Persian speech recognition.
-   **Intelligence Layer:** Integrated with **GPT-5.6 (GapGPT)** for complex intent recognition and sentiment analysis.
-   **Neural TTS:** Natural-sounding Persian voice synthesis using `Edge-TTS` (Dilara Neural).
-   **Enterprise UI:** A modern, Dark-themed dashboard with Glassmorphism design, featuring:
    -   Live Waveform Visualizer.
    -   Real-time Latency & Confidence metrics.
    -   System Operation Logs.
-   **Bare-metal Ready:** Optimized for Ubuntu 24.04 LTS and HP ProLiant environments.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, FastAPI |
| **Speech-to-Text** | Faster-Whisper (CTranslate2) |
| **Brain (LLM)** | GPT-5.6 via OpenAI API |
| **Text-to-Speech** | Microsoft Edge TTS |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JS |
| **Infrastructure** | Ubuntu / Docker Ready |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher.
- NVIDIA GPU with CUDA support (Recommended for < 2s latency).

### Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/your-username/asiatech-voice-bot.git
   cd asiatech-voice-bot
   
