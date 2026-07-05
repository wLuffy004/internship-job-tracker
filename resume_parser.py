from config import SKILL_KEYWORDS


def load_resume(file_path):
    """
    Read resume text from a txt file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def extract_resume_skills(resume_text):
    """
    Extract known skills from resume text.
    """
    resume_text = resume_text.lower()
    matched_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in resume_text:
            matched_skills.append(skill)

    return matched_skills