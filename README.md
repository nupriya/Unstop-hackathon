# 🔥 AttentionX AI – Automated Content Repurposing Engine

## 🚀 Overview

AttentionX AI is a multimodal AI-powered system that transforms long-form video content (lectures, podcasts, mentorship sessions) into short, engaging, viral-ready clips.

It automatically detects **high-impact “golden moments”**, converts them into **vertical social media format (9:16)**, and generates **captions + hooks** — making educational content snackable and shareable.

---

## 🎯 Problem Statement

Modern audiences consume content in short bursts, but valuable insights are buried inside long videos.

Challenges:

* ⏳ Manually finding important moments in long videos
* 📱 Converting horizontal videos into vertical format
* 📝 Creating engaging captions and hooks
* 🎬 Repurposing content efficiently for social media

---

## 💡 Solution

AttentionX solves this by using **multimodal AI (audio + text + vision)** to:

* 🧠 Extract transcript using speech-to-text
* 🔥 Detect emotional and high-value moments
* ✂️ Automatically generate short clips
* 🎯 Convert videos to vertical (9:16) format
* 💬 Generate catchy captions/hooks
* 📊 Visualize “viral peaks” using analytics

---

## 🧠 Core Features

### 🎧 Speech-to-Text (Whisper)

* Converts video audio into timestamped transcripts

### 🔥 Viral Moment Detection

* Detects impactful segments using:

  * Keyword importance
  * Sentence length
  * Heuristic scoring

### 📊 Emotional Peak Analysis

* Visualizes engagement spikes over time

### 🎬 Auto Clip Generator

* Extracts top 3 viral segments

### 📱 Smart Vertical Cropping

* Converts videos to 9:16 format for Reels/Shorts

### 💬 Caption & Hook Generator

* Generates attention-grabbing text for each clip

---

## 🏗️ Tech Stack

| Component        | Technology         |
| ---------------- | ------------------ |
| Frontend         | Streamlit          |
| Backend          | Python             |
| Speech-to-Text   | Whisper            |
| Video Processing | MoviePy            |
| Audio Analysis   | Librosa            |
| Computer Vision  | MediaPipe / OpenCV |
| Visualization    | Matplotlib         |

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/attentionx-ai.git
cd attentionx-ai
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install FFmpeg

Download from: https://ffmpeg.org/download.html
Add it to system PATH.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open:
👉 http://localhost:8501

---

## 🎥 Demo Video

👉 **Watch the working demo here:**
https://drive.google.com/file/d/144VuqfmlLuLITmNuOm8ofsWv3C-pioN0/view?usp=sharing

---

## 📂 Project Structure

```text
attentionx_ai/
│
├── app.py
├── requirements.txt
│
├── utils/
│   ├── audio.py
│   ├── clips.py
│   ├── captions.py
│   ├── viral_ai.py
│   ├── analytics.py
│   └── smart_crop.py
│
└── temp/
```

---

## 🏆 Why This Project Stands Out

* ✅ End-to-end automated pipeline
* ✅ Real-world Creator Economy use-case
* ✅ Multimodal AI (audio + text + vision)
* ✅ Clean and interactive UI
* ✅ Converts long content → viral short clips

---

## 🚀 Future Improvements

* 🎬 Auto subtitles on video
* 🧠 LLM-based intelligent clip selection (Gemini/OpenAI)
* 📱 Direct export to social media
* 🌐 Cloud deployment

---

## 👨‍💻 Author

**Nupriya Saxena**
AI/ML Developer 🚀

---

## 📜 License

For educational and hackathon use.

---

⭐ If you like this project, give it a star!
