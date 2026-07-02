import sqlite3
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from matcher import calculate_match_score, get_matched_skills, get_missing_skills


DB_NAME = "data/jobs.db"


def load_jobs():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df


def build_skill_frequency(df):
    all_skills = []

    for skill_text in df["skills"].fillna(""):
        skills = [skill.strip() for skill in skill_text.split(",") if skill.strip()]
        all_skills.extend(skills)

    skill_counter = Counter(all_skills)

    skill_df = pd.DataFrame(
        skill_counter.items(),
        columns=["Skill", "Frequency"]
    ).sort_values(by="Frequency", ascending=False)

    return skill_df


st.set_page_config(
    page_title="Internship Job Tracker Dashboard",
    layout="wide"
)

st.title("Internship Job Tracker & Skill Analyzer")
st.caption("Track internship jobs, analyze required skills, and explore job market patterns.")

jobs_df = load_jobs()

st.sidebar.header("Filters")

user_skills = st.sidebar.text_input(
    "Enter your skills",
    value="python, sql, git"
)

title_keyword = st.sidebar.text_input("Search by job title")
skill_keyword = st.sidebar.text_input("Search by skill")

company_options = sorted(jobs_df["company"].dropna().unique().tolist())
selected_companies = st.sidebar.multiselect(
    "Select companies",
    company_options,
    default=company_options
)

location_options = sorted(jobs_df["location"].dropna().unique().tolist())
selected_locations = st.sidebar.multiselect(
    "Select locations",
    location_options,
    default=location_options
)

filtered_df = jobs_df.copy()

if title_keyword:
    filtered_df = filtered_df[
        filtered_df["title"].fillna("").str.contains(title_keyword, case=False)
    ]

if skill_keyword:
    filtered_df = filtered_df[
        filtered_df["skills"].fillna("").str.contains(skill_keyword, case=False)
    ]

if selected_companies:
    filtered_df = filtered_df[filtered_df["company"].isin(selected_companies)]

if selected_locations:
    filtered_df = filtered_df[filtered_df["location"].isin(selected_locations)]

filtered_df = filtered_df.copy()

filtered_df["match_score"] = filtered_df["skills"].apply(
    lambda skills: calculate_match_score(skills, user_skills)
)

filtered_df["matched_skills"] = filtered_df["skills"].apply(
    lambda skills: get_matched_skills(skills, user_skills)
)

filtered_df["missing_skills"] = filtered_df["skills"].apply(
    lambda skills: get_missing_skills(skills, user_skills)
)

filtered_df = filtered_df.sort_values(by="match_score", ascending=False)


st.subheader("Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Filtered Jobs", len(filtered_df))

with col2:
    st.metric("Total Jobs", len(jobs_df))

with col3:
    st.metric("Companies", filtered_df["company"].nunique())

with col4:
    st.metric("Locations", filtered_df["location"].nunique())

with col5:
    if not filtered_df.empty:
        st.metric("Best Match", f"{filtered_df['match_score'].max()}%")
    else:
        st.metric("Best Match", "N/A")


st.subheader("Job Table")
st.dataframe(filtered_df, use_container_width=True)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Jobs as CSV",
    data=csv_data,
    file_name="filtered_jobs.csv",
    mime="text/csv"
)


st.subheader("Skill Frequency")

skill_df = build_skill_frequency(filtered_df)

if not skill_df.empty:
    st.dataframe(skill_df, use_container_width=True)

    st.subheader("Top Skills Chart")

    top_skills = skill_df.head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(top_skills["Skill"], top_skills["Frequency"])
    ax.set_xlabel("Skill")
    ax.set_ylabel("Frequency")
    ax.set_title("Top 10 Skills")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
else:
    st.info("No skill data found for the current filters.")


st.subheader("Top Companies Chart")

company_counts = (
    filtered_df["company"]
    .value_counts()
    .reset_index()
)

company_counts.columns = ["Company", "Job Count"]

if not company_counts.empty:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(company_counts["Company"], company_counts["Job Count"])
    ax.set_xlabel("Company")
    ax.set_ylabel("Job Count")
    ax.set_title("Jobs by Company")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
else:
    st.info("No company data found for the current filters.")