
# 🧠 Smart Resume Analyzer

A Streamlit-based web app that analyzes resumes to extract key information and recommend personalized skills and courses — powered by NLP and PDF processing.

---

## 🚀 Features

- 📄 Upload PDF resumes and extract:
  - Name
  - Email
  - Phone number
  - Skills
  - Resume page count
- 🔍 Automatic skill detection using keyword scanning
- 🎯 Predicts candidate’s likely job domain (Data Science, Web Dev, Android, etc.)
- 🎓 Recommends courses & certificates based on skills
- 🧠 Suggests interview prep videos and resume building tips
- 🔐 Admin panel to view all uploaded resumes with insights
- 💾 Stores data in MySQL for future analysis

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend/NLP**: Python, spaCy, nltk, pdfminer.six
- **Database**: MySQL
- **Extras**: yt-dlp for YouTube integration, streamlit-tags for skill UI

---

## 📸 Screenshots

| Resume Upload | Admin Panel |
|---------------|-------------|
| ![Upload](https://your-upload-screenshot.png) | ![Admin](https://your-admin-screenshot.png) |

> Replace these with your actual screenshots or use placeholders.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
