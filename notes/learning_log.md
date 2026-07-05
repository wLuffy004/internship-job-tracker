\# Learning Log



## Day 0-2



What I completed:

\- Checked Python and pip installation

\- Created project folder structure

\- Created sample internship job data in CSV format

\- Used pandas to read CSV data

\- Printed job records and total job count

\- Initialized Git repository

\- Connected local project to GitHub

\- Pushed the first commit to GitHub



What I learned:

\- Difference between Python and PowerShell

\- Difference between data and database

\- How CSV works as text-based table data

\- Basic Git workflow: add, commit, push

\- Meaning of main branch and origin/main

## Day 3-5

What I completed:

* Moved CSV loading logic into analysis.py

* Created a skill keyword list in config.py

* Built a function to extract skills from job descriptions

* Added a skills column to the job dataframe

* Counted skill frequency across all internship jobs

* Updated app.py to call functions from analysis.py

* Printed job records with extracted skills

* Printed skill frequency results

* Updated LeetCode log for Two Sum

* Practiced LeetCode 217: Contains Duplicate

What I learned:

* How to separate code into different Python files

* How to use import to reuse functions from another file

* How to store project configuration in config.py

* How to extract keywords from text data

* How to use a dictionary to count frequency

* Difference between a dictionary and a set

* Time complexity and space complexity of hash-based solutions

* Why hash tables can reduce time complexity from O(n²) to O(n)

## Day 6-8

What I completed:

* Added SQLite database support to the project

* Created database functions in database.py

* Created a jobs table in SQLite

* Saved job data from jobs.csv into data/jobs.db

* Loaded job data back from the SQLite database

* Used database data for skill extraction and skill frequency analysis

* Added duplicate prevention using apply_url as a unique field

* Used INSERT OR IGNORE to avoid duplicate job records

* Updated app.py to use the database workflow

* Added data/jobs.db to .gitignore

What I learned:

* SQLite is a lightweight database stored in a local .db file

* Difference between CSV storage and database storage

* How to create a database table using SQL

* How to insert data into a SQLite table from pandas

* How to load database records back into a pandas DataFrame

* Why unique fields help prevent duplicate records

* Why database logic should be separated into database.py

* Current project flow: CSV file -> SQLite database -> data analysis -> skill frequency output

## Day 9-11 - Streamlit Dashboard Development

Today I completed the Streamlit dashboard module for the Internship Job Tracker & Skill Analyzer project.

Completed:
- Added Streamlit and matplotlib to requirements.txt
- Built the first version of the Streamlit dashboard
- Displayed overview metrics including total jobs, companies, and locations
- Displayed the job table from the SQLite database
- Added skill frequency analysis and skill visualization charts
- Added a skills column to the SQLite jobs table
- Migrated and updated database records with extracted skills
- Connected the dashboard directly to the database
- Moved filters to the sidebar
- Added multi-select filters for companies and locations
- Added job title keyword search
- Added skill keyword search
- Added CSV download for filtered job results
- Improved dashboard layout and user experience
- Added screenshots to document progress

Key Progress:
The project now has a complete working pipeline:

CSV Job Data
-> Skill Extraction
-> SQLite Database Storage
-> Streamlit Dashboard Visualization

Reflection:
This milestone was important because it connected all previous modules into one complete workflow. The project is no longer just a collection of separate scripts. It now supports data storage, skill analysis, interactive filtering, and visual exploration through a dashboard. This makes the project much closer to a real-world data analysis application.

## Day 12-14 - Resume Match Score System and HashMap Practice

Today I added a resume skill matching system to the project and practiced more hash table problems.

Completed:
- Created matcher.py
- Added skill parsing functions
- Added match score calculation
- Added matched skills output
- Added missing skills output
- Connected match score logic to dashboard.py
- Sorted jobs by match score
- Added best match metric to the dashboard
- Practiced LeetCode 242: Valid Anagram
- Practiced LeetCode 383: Ransom Note

Reflection:
The project now helps compare user skills with internship requirements. I also practiced hash table frequency counting and learned how dictionary.get(key, default) works in Python.

## Day 15-17 - README, Project Cleanup, and Deployment

Today I polished the project and deployed the Streamlit dashboard online.

Completed:
- Improved README.md with project overview, features, tech stack, screenshots, setup steps, and future improvements
- Added the live demo link to README.md
- Checked requirements.txt
- Checked .gitignore
- Verified the project folder structure
- Fixed app.py so it preserves extracted skills when saving data to the database
- Updated dashboard.py to automatically initialize the SQLite database from CSV when deployed
- Deployed the dashboard to Streamlit Cloud
- Confirmed the live app can be opened online

Reflection:
This stage made the project much more professional. The project is no longer only a local script. It now has documentation, a GitHub portfolio page, and a live deployed dashboard that other people can access.

## Day 18-20 - UI Polish, Better Data, and Deployment Update

Today I improved the deployed Streamlit dashboard and polished the project for portfolio use.

Completed:
- Improved the dashboard title and sidebar layout
- Added clearer text for the skill input section
- Expanded sample job data from 5 jobs to 10 jobs
- Fixed skill frequency counting for database-loaded skill strings
- Cleaned the local SQLite database and regenerated it from the updated CSV data
- Confirmed the dashboard shows updated job data correctly
- Synced all changes to GitHub
- Confirmed Streamlit Cloud redeployed the latest version successfully

Reflection:
This update made the project look more complete and realistic. The dashboard now has better sample data, cleaner UI text, and a stable deployment workflow. The project is now strong enough to use as a portfolio MVP.