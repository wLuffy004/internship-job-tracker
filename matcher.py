def parse_skills(skill_text):
    """
    Convert a comma-separated skill string into a clean skill set.
    """
    if skill_text is None:
        return set()

    skills = [
        skill.strip().lower()
        for skill in str(skill_text).split(",")
        if skill.strip()
    ]

    return set(skills)


def calculate_match_score(job_skills, user_skills):
    """
    Calculate the percentage of job skills matched by the user.
    """
    job_skill_set = parse_skills(job_skills)
    user_skill_set = parse_skills(user_skills)

    if not job_skill_set:
        return 0

    matched_skills = job_skill_set.intersection(user_skill_set)
    score = len(matched_skills) / len(job_skill_set) * 100

    return round(score, 2)


def get_matched_skills(job_skills, user_skills):
    """
    Get skills that appear in both job skills and user skills.
    """
    job_skill_set = parse_skills(job_skills)
    user_skill_set = parse_skills(user_skills)

    return ", ".join(sorted(job_skill_set.intersection(user_skill_set)))


def get_missing_skills(job_skills, user_skills):
    """
    Get job skills that the user does not have yet.
    """
    job_skill_set = parse_skills(job_skills)
    user_skill_set = parse_skills(user_skills)

    return ", ".join(sorted(job_skill_set.difference(user_skill_set)))