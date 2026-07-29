import re

import pandas as pd

from config import SKILL_KEYWORDS


def load_jobs(file_path="data/jobs.csv"):
    """
    Load job data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df


def contains_skill(text, skill):
    """
    Check whether a skill appears as a complete word or phrase in text.
    """
    text = str(text).lower()
    skill = skill.lower()

    pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"
    return re.search(pattern, text) is not None


def extract_skills(description):
    """
    Extract known technical skills from a job description.
    """
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if contains_skill(description, skill):
            found_skills.append(skill)

    return found_skills


def add_skills_column(df):
    """
    Add a skills column to the job DataFrame.
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
        if isinstance(skills, list):
            skill_list = skills
        else:
            skill_list = [
                skill.strip()
                for skill in str(skills).split(",")
                if skill.strip()
            ]

        for skill in skill_list:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    return dict(
        sorted(
            skill_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )