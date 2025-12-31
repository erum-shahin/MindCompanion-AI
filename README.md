# 💙 MindCompanion - AI Mental Health Support

**MindCompanion** is an intelligent mental health chatbot designed to provide immediate, empathetic support to students. unlike standard chatbots, it uses **Google's Gemini 2.5 Flash** to perform real-time sentiment analysis, calculating a "Stress Score" and detecting emotional states (Mood) as the user types.

> **Built for the TechSprint by GDGoc Academy Of Technology Hackathon 2025**

## 🚀 Key Features
* **Real-time Analysis:** Detects user mood (e.g., Anxious, Calm, Overwhelmed) instantly.
* **Clinical Stress Scoring:** Assigns a stress score (1-10) to every interaction to help identify high-risk situations.
* **Advanced AI Engine:** Powered by Google's **Gemini 2.5 Flash / 2.0** models for nuanced understanding.
* **Privacy-First:** No data is stored permanently; sessions are ephemeral.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Backend:** Google Gemini API
* **Language:** Python 3.10+

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/MindCompanion.git](https://github.com/YOUR_USERNAME/MindCompanion.git)
    cd MindCompanion
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Keys**
    * Create a file named `.env` in the main folder.
    * Add your Google API key:
    ```text
    GOOGLE_API_KEY=your_api_key_here
    ```

4.  **Run the App**
    ```bash
    streamlit run web.py
    ```

## 📸 Usage
Once the app is running, simply type how you are feeling. The sidebar will update in real-time to show your **Current Mood** and **Stress Level** based on the AI's analysis of your text.

## 🤝 Contributing
This is a hackathon project, but feel free to fork and improve!

---
*Made with 💙 by Team AlgoRythm*
