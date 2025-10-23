# 📊 WhatsApp Chat Analysis Dashboard

An interactive Python application to parse, analyze, and visualize WhatsApp chat data, providing insights into user activity and conversation trends.

---
**screenshots**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c5b86ca4-2409-476d-902d-93e60eb5fe8b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2371f0e3-7305-4e3f-8750-a15d178f6e66" />

## ✨ Key Features

- **💬 Comprehensive Chat Parsing**: Converts exported WhatsApp chats into structured data with timestamps, users, messages, and derived columns like day, month, and hour.  
- **📈 Activity Analysis**: Generate daily, weekly, and monthly activity timelines. Identify busiest days and peak messaging hours.  
- **👥 User Insights**: Detect most active participants and visualize individual or group activity patterns.  
- **📊 Interactive Visualization**: Explore trends through charts and timelines via an intuitive Streamlit interface.

---

## 🛠 Tech Stack

- **🐍 Python 3** – Core language  
- **📊 Pandas** – Data wrangling and analysis  
- **🔍 Regex** – Parsing chat text  
- **🌐 Streamlit** – Interactive web application  
- **📉 Matplotlib / Seaborn** – Data visualization  
- **💻 VS Code** – Development environment  

---

## ⚡ How It Works

1. **📂 Upload WhatsApp Chat**: Provide a `.txt` export of the chat.  
2. **🧹 Preprocessing**: `preprocessor.py` converts raw chat into a clean DataFrame with columns:  
   `date`, `only_date`, `user`, `message`, `year`, `month`, `month_num`, `day`, `day_name`, `hour`.  
3. **📊 Analysis**: `helper.py` computes:
   - Daily & monthly timelines  
   - Most active users  
   - Weekly activity patterns  
4. **📈 Visualization**: Streamlit displays interactive charts and summaries for quick insights.

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone <repo-url>
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


