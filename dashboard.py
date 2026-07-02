import sqlite3
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


DB_NAME = "data/jobs.db"


def load_jobs():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df


st.set_page_config(
    page_title="Internship Job Tracker Dashboard",
    layout="wide"
)

st.title("Internship Job Tracker & Skill Analyzer")

jobs_df = load_jobs()

st.subheader("Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(jobs_df))

with col2:
    st.metric("Companies", jobs_df["company"].nunique())

with col3:
    st.metric("Locations", jobs_df["location"].nunique())


st.subheader("Filters")

filtered_df = jobs_df.copy()

companies = ["All"] + sorted(jobs_df["company"].dropna().unique().tolist())
selected_company = st.selectbox("Select Company", companies)

if selected_company != "All":
    filtered_df = filtered_df[filtered_df["company"] == selected_company]

locations = ["All"] + sorted(jobs_df["location"].dropna().unique().tolist())
selected_location = st.selectbox("Select Location", locations)

if selected_location != "All":
    filtered_df = filtered_df[filtered_df["location"] == selected_location]

skill_keyword = st.text_input("Search Skill")

if skill_keyword:
    filtered_df = filtered_df[
        filtered_df["skills"].fillna("").str.contains(skill_keyword, case=False)
    ]


st.subheader("Job Table")
st.dataframe(filtered_df, use_container_width=True)


st.subheader("Skill Frequency")

all_skills = []

for skill_text in filtered_df["skills"].dropna():
    skills = [skill.strip() for skill in skill_text.split(",") if skill.strip()]
    all_skills.extend(skills)

skill_counter = Counter(all_skills)

skill_df = pd.DataFrame(
    skill_counter.items(),
    columns=["Skill", "Frequency"]
).sort_values(by="Frequency", ascending=False)

st.dataframe(skill_df, use_container_width=True)


st.subheader("Top Skills Chart")

top_skills = skill_df.head(10)

if not top_skills.empty:
    fig, ax = plt.subplots()
    ax.bar(top_skills["Skill"], top_skills["Frequency"])
    ax.set_xlabel("Skill")
    ax.set_ylabel("Frequency")
    ax.set_title("Top 10 Skills")
    plt.xticks(rotation=45)
    st.pyplot(fig)