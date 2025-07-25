🧠 Smart Resume Analyzer
A Streamlit-powered AI Resume Analyzer that reads resumes (PDF), extracts key details, identifies skill gaps, and recommends personalized learning resources — all in seconds. Built for students, job seekers, and recruiters.

📌 Features
📄 PDF Resume Upload & Parsing

🧠 NLP-based Skill Extraction

🎯 Job Field & Candidate Level Prediction

💡 Recommended Skills & Online Courses

📊 Admin Dashboard with Visual Analytics

📽️ Bonus: Resume & Interview Tips (YouTube)

🚀 Tech Stack
Layer	              Technology Used
🧠 NLP/Parsing	    pdfminer, nltk, re, spaCy
💻 Frontend	        Streamlit, streamlit-tags, plotly
🛢️ Database	        Supabase (PostgreSQL)
🔗 Extras	          yt-dlp for YouTube video scraping

🌐 Live Demo
🟢 https://resume-analyzer001.streamlit.app
Public deployment available for testing.

📁 Setup Instructions
1.Clone the repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
2.Install dependencies
pip install -r requirements.txt
3.Add your Supabase credentials
Create a .streamlit/secrets.toml file:
[db]
host = "your-db-host"
port = "5432"
database = "your-database-name"
user = "your-username"
password = "your-password"
4.Run the app
streamlit run App.py
👤 Admin Login
Use this to access the dashboard:
Username: admin_bhumik
Password: 198200
📊 Sample Screenshots



🎯 Problem Statement
Job seekers often lack clarity on skill gaps and relevant courses, while recruiters waste time manually reviewing resumes.
This tool automates resume analysis and recommends improvements using NLP and ML.

📌 Alignment with Hackathon Proposal
✅ Core idea: Resume parsing + skill recommendations

✅ Enhancement: Admin analytics dashboard

✅ Innovation: Bonus YouTube tips and course links

👥 Team
Name	        Role
Bhumik Kundu	Full-stack Developer & ML Engineer

📜 License
MIT License (or any license you prefer)

