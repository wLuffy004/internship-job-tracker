from analysis import load_jobs, add_skills_column, count_skill_frequency


def main():
    df = load_jobs()
    df = add_skills_column(df)

    print("Total jobs:", len(df))

    print("\nJobs with extracted skills:")
    print(df[["title", "company", "location", "skills"]].to_string(index=False))

    print("\nSkill frequency:")
    skill_counts = count_skill_frequency(df)

    for skill, count in skill_counts.items():
        print(f"{skill}: {count}")


if __name__ == "__main__":
    main()