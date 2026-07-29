import re

from config import SKILL_KEYWORDS


def load_resume(file_path):
    """
    Read resume text from a .txt file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def contains_skill(text, skill):
    """
    Check whether a skill appears as a complete word or phrase in text.
    """
    text = str(text).lower()
    skill = skill.lower()

    pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"
    return re.search(pattern, text) is not None


def extract_resume_skills(resume_text):
    """
    Extract known technical skills from resume text.
    """
    matched_skills = []

    for skill in SKILL_KEYWORDS:
        if contains_skill(resume_text, skill):
            matched_skills.append(skill)

    return matched_skills