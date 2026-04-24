
<div align="center">

```
██████╗ ██████╗ ██╗███████╗███████╗███╗   ███╗██╗███╗   ██╗██████╗ 
██╔══██╗██╔══██╗██║██╔════╝██╔════╝████╗ ████║██║████╗  ██║██╔══██╗
██████╔╝██████╔╝██║█████╗  █████╗  ██╔████╔██║██║██╔██╗ ██║██║  ██║
██╔══██╗██╔══██╗██║██╔══╝  ██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║  ██║
██████╔╝██║  ██║██║███████╗██║     ██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ 
```

### ⚡ Executive Document Intelligence · Powered by Groq LPU + Llama 3.3 70B

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq_LPU-00C7B7?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Llama](https://img.shields.io/badge/Llama_3.3_70B-a855f7?style=for-the-badge&logo=meta&logoColor=white)](https://ai.meta.com)
[![License](https://img.shields.io/badge/License-MIT-f472b6?style=for-the-badge)](LICENSE)

<br/>

> *"From pages of noise to moments of signal — BriefMind compresses intelligence at the speed of thought."*

</div>

---

## 🌌 What is BriefMind?

**BriefMind** is a next-generation AI document summarization engine that transforms dense, long-form documents into crisp, executive-grade intelligence — in seconds, not minutes.

Built on **Groq's LPU (Language Processing Unit)** — the fastest inference hardware on the planet — and powered by **Meta's Llama 3.3 70B**, BriefMind doesn't just summarize. It *understands*, *distills*, and *delivers* knowledge at superhuman speed.

Whether you're a researcher, analyst, executive, or student drowning in text — BriefMind is your cognitive co-pilot.

---

## 🚀 Core Capabilities

| Feature | Description |
|--------|-------------|
| ⚡ **Groq LPU Inference** | Sub-second AI generation via dedicated Language Processing Units |
| 🧠 **Llama 3.3 70B** | State-of-the-art 70 billion parameter model for elite comprehension |
| 🌊 **Real-Time Streaming** | Watch intelligence materialize word-by-word with live cursor feedback |
| 🎨 **Glassmorphic UI** | Cyber-dark aesthetic with gradient accents, blurred cards, and polished typography |
| 📄 **Multi-Format Ingestion** | Plug in `.txt` and `.csv` files — drag, drop, done |
| 🛡️ **Secure by Design** | API key loaded via `.env` — never hardcoded, never exposed |
| 🏗️ **Scalable Architecture** | Streamlit-powered for frictionless local or cloud deployment |

---

## 🖥️ System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    BriefMind Interface                   │
│                                                          │
│  ┌─────────────────┐       ┌──────────────────────────┐  │
│  │   File Upload   │──────▶│    Streamlit Frontend    │ │
│  │  (.txt / .csv)  │       │   (Glassmorphic Theme)   │  │
│  └─────────────────┘       └─────────────┬────────────┘  │
│                                          │               │
│                             ┌────────────▼────────────┐  │
│                             │     Groq API Client     │  │
│                             │   (Streaming Mode ON)   │  │
│                             └────────────┬────────────┘  │
│                                          │               │
│                             ┌────────────▼────────────┐  │
│                             │   Llama 3.3 70B Model   │  │
│                             │   via Groq LPU Cloud    │  │
│                             └────────────┬────────────┘  │
│                                          │               │
│                             ┌────────────▼────────────┐  │
│                             │  Executive Summary Out  │  │
│                             │   (Streamed, Live UI)   │  │
│                             └─────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## 📦 Prerequisites

Before you launch, make sure your system is equipped:

- **Python** `3.10+`
- A **[Groq API Key](https://console.groq.com)** — free tier available
- A terminal and 60 seconds of your time

---

## ⚙️ Installation

### 1 · Clone the Repository

```bash
git clone https://github.com/shakeelscribes/Document-summarizer.git
cd Document-summarizer
```

### 2 · Install Dependencies

```bash
pip install -r requirements.txt
```

### 3 · Set Up Your Environment

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)

### 4 · Launch BriefMind

```bash
streamlit run docs.py
```

Then open your browser at `http://localhost:8501` — and witness the future of document intelligence.

---

## 🧪 Usage

```
1.  Launch the app via Streamlit
2.  Drop your .txt or .csv document into the upload zone
3.  Review your raw document in the left panel
4.  Click  ✨ GENERATE INTELLIGENCE
5.  Watch your executive summary materialize in real time
```

---

## 📁 Project Structure

```
Document-summarizer/
│
├── docs.py              # 🧠 Core application — UI, streaming, Groq integration
├── requirements.txt     # 📦 Python dependencies
├── .env                 # 🔐 API key config (create this yourself)
└── README.md            # 📖 You are here
```

---

## 🔮 Roadmap — What's Next

The current build is a high-performance MVP. Here's what's on the horizon:

- [ ] 🗂️ **PDF & DOCX support** — go beyond `.txt` and `.csv`
- [ ] 🌐 **Multi-language summaries** — break the language barrier
- [ ] 📊 **Structured output modes** — bullet points, TLDR, or full executive brief
- [ ] 💾 **Export to PDF/DOCX** — take your summary anywhere
- [ ] 🧵 **Multi-document batch processing** — summarize entire folders at once
- [ ] 🔌 **API endpoint** — integrate BriefMind into your own stack
- [ ] 🗣️ **Voice output** — have your summary read aloud

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit + Custom CSS (Glassmorphism) |
| **AI Model** | Llama 3.3 70B Versatile |
| **Inference Engine** | Groq LPU Cloud |
| **Language** | Python 3.10+ |
| **Env Management** | python-dotenv |
| **Streaming** | Groq Chat Completions Streaming API |

---

## 🤝 Contributing

Contributions, ideas, and pull requests are warmly welcomed.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request 🚀
```

---

## 📜 License

This project is open-source under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ⚡ by [shakeelscribes](https://github.com/shakeelscribes)**

*Compressing the world's knowledge — one document at a time.*

</div>
