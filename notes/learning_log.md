# Learning Log

## Day 0-2 - Project Setup and CSV Data

Today I created the initial structure of the Internship Job Tracker project and learned the basic workflow for Python, CSV data, Git, and GitHub.

Completed:
- Checked the Python and pip installation
- Created the project folder structure
- Created sample internship job data in CSV format
- Used pandas to read CSV data
- Printed job records and the total job count
- Initialized a local Git repository
- Connected the local project to GitHub
- Created and pushed the first commit

Reflection:
This stage helped me understand the difference between Python and PowerShell, the difference between data and databases, and how CSV files store table-like information. I also learned the basic Git workflow of adding, committing, and pushing changes, as well as the meaning of the main branch and origin/main.


## Day 3-5 - Skill Extraction and Frequency Analysis

Today I separated the project into reusable Python modules and added technical skill extraction and frequency analysis.

Completed:
- Moved CSV loading logic into analysis.py
- Created a skill keyword list in config.py
- Built a function to extract skills from job descriptions
- Added a skills column to the job DataFrame
- Counted skill frequency across internship job postings
- Updated app.py to call functions from analysis.py
- Printed job records with extracted skills
- Printed skill frequency results
- Updated the LeetCode log for Two Sum
- Practiced LeetCode 217: Contains Duplicate

Reflection:
This stage taught me how to organize Python code across multiple files and reuse functions with imports. I also learned how to store configuration values in config.py, extract keywords from text, count frequencies with dictionaries, and choose between dictionaries and sets. The LeetCode exercises helped me understand why hash tables can reduce time complexity from O(n²) to O(n).


## Day 6-8 - SQLite Database Integration

Today I added SQLite database support and connected the data analysis workflow to persistent database storage.

Completed:
- Added SQLite database support to the project
- Created database functions in database.py
- Created a jobs table in SQLite
- Saved job data from jobs.csv into data/jobs.db
- Loaded job records from the SQLite database
- Used database data for skill extraction and frequency analysis
- Added duplicate prevention using apply_url as a unique field
- Used database conflict handling to prevent duplicate job records
- Updated app.py to use the database workflow
- Added data/jobs.db to .gitignore

Reflection:
This stage helped me understand that SQLite is a lightweight database stored in a local file. I learned the difference between CSV storage and database storage, how to create SQL tables, how to insert pandas data into SQLite, and how to load database records into a DataFrame. I also learned why database logic should be separated into database.py and why unique fields are important for preventing duplicate data.


## Day 9-11 - Streamlit Dashboard Development

Today I completed the first interactive Streamlit dashboard for the Internship Job Tracker & Skill Analyzer project.

Completed:
- Added Streamlit and matplotlib to requirements.txt
- Built the first version of the Streamlit dashboard
- Displayed overview metrics for jobs, companies, and locations
- Displayed the job table from the SQLite database
- Added skill frequency analysis and visualization
- Added a skills column to the SQLite jobs table
- Migrated and updated database records with extracted skills
- Connected the dashboard directly to the database
- Moved filters to the sidebar
- Added multi-select filters for companies and locations
- Added job title keyword search
- Added skill keyword search
- Added CSV download for filtered job results
- Improved the dashboard layout and user experience
- Added screenshots to document progress

Reflection:
This milestone connected the previous modules into one complete workflow:

```text
CSV Job Data
-> Skill Extraction
-> SQLite Database Storage
-> Streamlit Dashboard Visualization
```

The project was no longer a collection of separate scripts. It could now store data, analyze skills, filter internship records, and present results through an interactive interface.


## Day 12-14 - Resume Match Score System and Hash Table Practice

Today I added a skill matching system and practiced additional hash table problems.

Completed:
- Created matcher.py
- Added skill parsing functions
- Added match score calculation
- Added matched skills output
- Added missing skills output
- Connected match score logic to dashboard.py
- Sorted jobs by match score
- Added a best match metric to the dashboard
- Practiced LeetCode 242: Valid Anagram
- Practiced LeetCode 383: Ransom Note

Reflection:
The project could now compare user skills with internship requirements and rank jobs by compatibility. I also practiced hash table frequency counting and learned how dictionary.get(key, default) works in Python.


## Day 15-17 - README, Project Cleanup, and Deployment

Today I improved the project documentation, cleaned the repository, and deployed the Streamlit dashboard online.

Completed:
- Improved README.md with a project overview, features, tech stack, screenshots, setup steps, and future improvements
- Added the live demo link to README.md
- Checked requirements.txt
- Checked .gitignore
- Verified the project folder structure
- Fixed app.py so extracted skills are preserved when saving data to the database
- Updated dashboard.py to initialize the SQLite database automatically from CSV data
- Deployed the dashboard to Streamlit Cloud
- Confirmed that the live application could be opened online

Reflection:
This stage made the project more professional and accessible. The application was no longer limited to my local computer. It had complete documentation, a public GitHub repository, and a live dashboard that other users could access.


## Day 18-20 - UI Polish, Better Data, and Deployment Update

Today I improved the deployed dashboard and expanded the sample internship data.

Completed:
- Improved the dashboard title and sidebar layout
- Added clearer instructions for the skill input section
- Expanded the sample job data from 5 jobs to 10 jobs
- Fixed skill frequency counting for database-loaded skill strings
- Cleaned the local SQLite database
- Regenerated the database from the updated CSV data
- Confirmed that the dashboard displayed the updated data correctly
- Synced all changes to GitHub
- Confirmed that Streamlit Cloud redeployed the latest version

Reflection:
This update made the dashboard more complete and realistic. It now had better sample data, clearer interface text, and a stable deployment workflow. At this stage, the project became strong enough to function as a portfolio MVP.


## Day 21-23 - Resume Parser and Dashboard Enhancements

Today I added resume text parsing and expanded the dashboard with stronger job matching and analytics features.

Completed:
- Created a resumes folder
- Added sample_resume.txt for testing
- Created resume_parser.py
- Added a function to load resume text from a .txt file
- Added resume skill extraction using the existing skill keyword list
- Connected resume upload to the Streamlit dashboard
- Added automatic skill extraction from uploaded resume text
- Used extracted resume skills to calculate job match scores
- Added a Best Matching Job section
- Added a Jobs by Location chart
- Added new screenshots for resume upload and dashboard analytics

Reflection:
This update made the project closer to a practical internship assistant. Users no longer needed to enter every skill manually because the dashboard could extract known technical skills from an uploaded text resume and use them to rank internship opportunities.


## Day 24-25 - Portfolio Version 1.0 Final Review

Today I completed the final portfolio review and prepared the Internship Job Tracker & Skill Analyzer for Portfolio Version 1.0.

Completed:
- Performed a complete review of the GitHub repository
- Reviewed README.md, requirements.txt, .gitignore, source code, screenshots, and learning notes
- Updated the README description from full-stack to end-to-end for greater technical accuracy
- Improved the live demo link presentation
- Updated the project structure to match the actual repository files
- Corrected screenshot filenames and README image references
- Clarified that data/jobs.db is generated automatically at runtime
- Replaced the informal license statement with a Project Status section
- Verified that the four dashboard screenshots exist and load correctly
- Verified the Streamlit Cloud deployment
- Reviewed the database, skill extraction, matching, and resume parser modules
- Standardized the formatting of all learning log entries
- Prepared the project to enter maintenance mode instead of continued large-scale feature development

Reflection:
This final review helped me understand that completing a software project includes more than writing code. A portfolio-ready project also needs accurate documentation, consistent file organization, a stable deployment, clear screenshots, and maintainable source code. Portfolio Version 1.0 is now feature-complete, and future updates will focus on bug fixes, documentation improvements, and deployment stability.