# Internship Job Tracker & Skill Analyzer

A full-stack internship tracking and skill analysis dashboard built with Python, SQLite, and Streamlit.

This project was developed as part of my Computer Science portfolio to practice data processing, database management, dashboard development, and software engineering workflow.

## Live Demo

🔗 https://internship-job-tracker-fdtpptf275ru5mysxvnkqd.streamlit.app/

This project helps users collect internship job data, extract required skills from job descriptions, store job records in a SQLite database, analyze resume-job matching, and explore the data through an interactive Streamlit dashboard.

---

## Features

- Load internship job data from CSV files
- Extract technical skills from job descriptions
- Count skill frequency across job postings
- Store job records in a SQLite database
- Prevent duplicate job records using apply URLs
- Display job data in an interactive Streamlit dashboard
- Filter jobs by title, company, location, and skill
- Upload a resume (.txt) and automatically extract skills
- Calculate resume-job match scores
- Display matched skills and missing skills
- Identify the best matching internship
- Visualize top skills, companies, and job locations
- Download filtered job results as a CSV file

---

## Tech Stack

- Python
- pandas
- SQLite
- Streamlit
- matplotlib
- Git & GitHub

---

## Project Structure

```text
internship-job-tracker/
├── app.py
├── analysis.py
├── config.py
├── dashboard.py
├── database.py
├── matcher.py
├── resume_parser.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── jobs.csv
│   └── jobs.db
│
├── resumes/
│   └── sample_resume.txt
│
├── screenshots/
│   ├── day21_23_01_resume_upload.png
│   ├── day21_23_02_best_matching_job.png
│   ├── day21_23_03_skill_frequency_chart.png
│   └── day21_23_04_location_chart.png
│
└── notes/
    ├── learning_log.md
    └── leetcode_log.md
```

---

## Dashboard Preview

### Dashboard Overview and Resume Matching

![Dashboard Overview and Resume Matching](screenshots/day21_23_01_dashboard_overview_resume_matching.png)

### Skill Frequency Analysis

![Skill Frequency Analysis](screenshots/day21_23_02_dashboard_skill_frequency_analysis.png)

### Company Distribution

![Company Distribution](screenshots/day21_23_03_dashboard_company_distribution.png)

### Location Distribution

![Location Distribution](screenshots/day21_23_04_dashboard_location_distribution.png)

---

## How It Works

The project follows this workflow:

```text
CSV Job Data
        │
        ▼
Skill Extraction
        │
        ▼
SQLite Database
        │
        ▼
Resume Upload
        │
        ▼
Resume Skill Extraction
        │
        ▼
Match Score Analysis
        │
        ▼
Interactive Streamlit Dashboard
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/wLuffy004/internship-job-tracker.git
cd internship-job-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

First, process the internship data:

```bash
python app.py
```

Then launch the dashboard:

```bash
streamlit run dashboard.py
```

---

## Resume Match Score

Users can either:

- Upload a resume text file (.txt)
- Or manually enter their skills

The dashboard automatically compares user skills with internship requirements and displays:

- Match Score
- Matched Skills
- Missing Skills
- Best Matching Internship

This helps users quickly identify suitable internship opportunities and understand which technical skills should be improved.

---

## Learning Goals

This project was built to practice:

- Python programming
- Data processing with pandas
- Python data structures (Hash Tables, Lists, Sets)
- SQLite database operations
- Streamlit dashboard development
- Resume-job matching
- Git & GitHub workflow
- Software project documentation
- Portfolio development

---

## Future Improvements

- Support PDF resume parsing
- Add NLP-based resume skill extraction
- Integrate real internship job scraping
- Improve dashboard analytics
- Add unit testing
- Build an AI-powered job recommendation system

---

## License

This project was created for educational purposes and portfolio demonstration.