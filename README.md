# 🧠 Anime Character Classifier 🎌

<img src="sample_results/Screenshot (29).png" width="100%" alt="Anime Classifier Demo Banner">

A Deep Learning-powered Anime Face Classifier built with 💥 TensorFlow, 🧪 CNN, and 🌐 Streamlit. Upload any anime face and the model predicts the most likely character in real-time!

---

## 🚀 Live Demo (Optional)
> 🔗 Coming soon! (Deploy to Streamlit Cloud or Hugging Face)

---

## ✨ Features

- 🔍 Classifies 5 anime characters:
  - Emilia (Re:Zero)
  - Satoru Gojo (Jujutsu Kaisen)
  - Hua Cheng (TGCF)
  - Monkey D. Luffy (One Piece)
  - Okabe Rintarou (Steins;Gate)
- 🧠 Trained from scratch using a custom-built CNN
- 📸 Real-time predictions with confidence scores
- 🖼️ Dataset scraped from DuckDuckGo
- 💻 Web UI built with Streamlit
- ⚙️ Clean project structure for extension and scaling

---

## 🛠 Tech Stack

| Tool         | Use                               |
|--------------|------------------------------------|
| TensorFlow | Deep learning model                |
| Keras      | CNN model architecture             |
| PIL, NumPy | Image preprocessing               |
| Streamlit  | Web app interface                  |
| DuckDuckGo | Anime image dataset scraping       |
| Git + GitHub | Version control + Portfolio showoff |

---

## 🧪 How to Run Locally

`bash
# 1. Clone this repo
git clone https://github.com/AO7108/anime-face-classifier.git
cd anime-face-classifier

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run anime_classifier_app.py

### 🧪 Sample Prediction

<img src="sample_results/Screenshot (45).png" width="70%">

