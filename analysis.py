import pandas as pd
from config import SKILL_KEYWORDS


def load_jobs(file_path="data/jobs.csv"):
    """
    Load job data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df


def extract_skills(description):
    """
    Extract skills from a job description.
    """
    description = str(description).lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in description:
            found_skills.append(skill)

    return found_skills


def add_skills_column(df):
    """
    Add a new column called 'skills' to the job dataframe.
    """
    df = df.copy()
    df["skills"] = df["description"].apply(extract_skills)
    return df


def count_skill_frequency(df):
    """
    Count how many times each skill appears across all jobs.
    """
    skill_counts = {}

    for skills in df["skills"]:
        for skill in skills:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    sorted_skill_counts = dict(
        sorted(skill_counts.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_skill_counts
