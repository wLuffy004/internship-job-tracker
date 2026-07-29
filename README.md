# Internship Job Tracker & Skill Analyzer

An end-to-end internship tracking and skill analysis application built with Python, SQLite, and Streamlit.

It helps internship seekers organize job opportunities, identify in-demand technical skills, evaluate resume-job fit, and explore internship data through an interactive dashboard.

## Live Demo

🚀 **[Open Live Demo](https://internship-job-tracker-fdtpptf275ru5mysxvnkqd.streamlit.app/)**

## Key Features

- Import and manage internship job data
- Extract technical skills from job descriptions
- Store job records in SQLite with duplicate prevention
- Filter jobs by title, company, location, and skill
- Upload a resume text file and automatically extract technical skills
- Calculate resume-job match scores
- Identify matched and missing skills
- Find the best matching internship opportunities
- Visualize skill demand, companies, and job locations
- Download filtered job results as CSV

---

## Dashboard Preview

### Dashboard Overview & Resume Matching

![Dashboard Overview and Resume Matching](screenshots/day21_23_01_dashboard_overview_resume_matching.png)

### Skill Frequency Analysis

![Skill Frequency Analysis](screenshots/day21_23_02_dashboard_skill_frequency_analysis.png)

<details>
<summary><strong>More Dashboard Analytics</strong></summary>

### Company Distribution

![Company Distribution](screenshots/day21_23_03_dashboard_company_distribution.png)

### Location Distribution

![Location Distribution](screenshots/day21_23_04_dashboard_location_distribution.png)

</details>

---

## Tech Stack

- **Python** — application logic and data processing
- **pandas** — internship data manipulation and analysis
- **SQLite** — persistent job storage
- **Streamlit** — interactive web dashboard
- **matplotlib** — data visualization
- **Git & GitHub** — version control and project management

---

## Technical Highlights

- Modular Python architecture separating data analysis, database, matching, resume parsing, and dashboard logic
- SQLite persistence with unique application URLs and conflict handling to prevent duplicate job records
- Rule-based technical skill extraction from internship descriptions and resume text
- Set-based resume-job matching using matched and missing skill analysis
- Automatic SQLite database initialization from CSV data when the database is unavailable
- Interactive filtering and ranking of internships by title, company, location, skill, and match score
- Downloadable filtered results for further analysis

---

## How It Works

The application follows this workflow:

```text
Internship Job Data (CSV)
          │
          ▼
Technical Skill Extraction
          │
          ▼
SQLite Database
          │
          ▼
Interactive Job Filtering
          │
          ▼
Resume / Skill Input
          │
          ▼
Resume Skill Extraction
          │
          ▼
Resume-Job Match Analysis
          │
          ▼
Ranking & Data Visualization
```

The dashboard compares the user's skills with the technical skills required by each internship and calculates a match score.

Jobs are then ranked by compatibility while showing:

- Match Score
- Matched Skills
- Missing Skills
- Best Matching Job

---

## Core Project Structure

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
│   └── jobs.db  # Generated automatically at runtime
│
├── resumes/
│   └── sample_resume.txt
│
└── screenshots/
    ├── day21_23_01_dashboard_overview_resume_matching.png
    ├── day21_23_02_dashboard_skill_frequency_analysis.png
    ├── day21_23_03_dashboard_company_distribution.png
    └── day21_23_04_dashboard_location_distribution.png
```

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/wLuffy004/internship-job-tracker.git
cd internship-job-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the dashboard

```bash
streamlit run dashboard.py
```

The application automatically creates and populates the SQLite database from the CSV dataset if the database does not already exist.

### Optional: Run the data processing workflow

```bash
python app.py
```

This processes the internship dataset, stores records in SQLite, and displays extracted skills and skill-frequency results in the terminal.

---

## Resume Matching

Users can either:

- Upload a `.txt` resume
- Manually enter technical skills

The application extracts recognized technical skills and compares them with the requirements of each internship.

For each job, the match score is calculated as:

```text
Match Score = Matched Required Skills / Total Required Skills × 100
```

The dashboard then ranks internship opportunities and displays the strongest match along with matched and missing skills.

---

## Database Design

Internship records are stored in a SQLite database.

Each job contains:

- Title
- Company
- Location
- Description
- Application URL
- Source
- Extracted Skills

The application URL is used as a unique field to prevent duplicate job records. Existing records are updated when the same application URL is encountered again.

---

## Project Status

**Version 1.0 is feature-complete and deployed.**

Current maintenance focuses on bug fixes, documentation improvements, and deployment stability.
