\# Learning Log



\## Day 0-2



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

