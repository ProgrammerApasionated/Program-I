# 📊 Life Report — Personal Activity Analysis Project

This project analyzes daily data related to steps, sleep, calories, and distance in order to generate a complete report that summarizes habits, consistency, and personal progress.  
The goal is to transform everyday data into a clear and meaningful view of daily life.
---
The program is able to:
- Read data from a text file
- Compute general statistics
- Detect standout days
- Classify each day based on custom criteria
- Identify relevant streaks
- Append new daily entries directly to the data file
---
## 🧠 What does the program do?

Given a data file with lines formatted as:

YYYY-MM-DD#steps#sleep_hours#calories#distance

The system processes all entries and generates a report including:

- Total and average step counts
- Most active and most demanding days
- Day classification (good, average, bad)
- Streaks related to steps, sleep, distance, and calories
- A final interpretative summary
---
## ▶️ How to run it

1. Make sure Python is installed on your system.
2. Place your data in the corresponding data file.
3. Run:


The report will be printed directly to the console.

📌 Example output :

📊 GENERAL STATISTICS
• Total steps: 891670
• Average sleep hours: 10.38

🌟 HIGHLIGHTED DAYS
• Most demanding day (calories): 2026-01-17 — 2620 kcal
• Most active day (distance): 2026-01-17 — 11.9 km

🎨 DAY CLASSIFICATION
• Good days: 48
• Average days: 0
• Bad days: 0

🔥 STREAKS
• Steps (>8000): 48 consecutive days
• Sleep (>7h): 48 consecutive days
• Distance (>5km): 48 consecutive days

### ✨ Why this project exists

- This project was born from a mix of technical curiosity and personal reflection.
- Each line in the data file represents a day lived, and each report is a way to observe habits, discipline, and long-term consistency.
- It is a small but meaningful project that combines programming, real data, and a conscious look at everyday life.
---
### 🛠️Future improvements
- Export reports to external files
- Add visual charts and graphs
- Build a fully interactive menu
- Fine-tune classification criteria based on personal preferences
---
### 🧑‍💻 Author
- Project developed by Álvaro as part of his learning journey in programming and data analysis.
---
### Is it over?
- My Programming I class is over, but my work will stay here.
- This repository will not grow with new files, but I will continue updating and improving the project over time.