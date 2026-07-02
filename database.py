import sqlite3
import pandas as pd


DB_PATH = "data/jobs.db"


def create_connection(db_path=DB_PATH):
    """
    Create a connection to the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    return conn


def get_table_columns(conn, table_name):
    """
    Get all column names from a table.
    """
    cursor = conn.execute(f"PRAGMA table_info({table_name});")
    columns = [row[1] for row in cursor.fetchall()]
    return columns


def create_jobs_table(conn):
    """
    Create the jobs table if it does not already exist.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_url TEXT UNIQUE,
        source TEXT,
        skills TEXT
    );
    """

    conn.execute(create_table_sql)
    conn.commit()


def migrate_jobs_table(conn):
    """
    Add missing columns to the jobs table.
    """
    columns = get_table_columns(conn, "jobs")

    if "skills" not in columns:
        conn.execute("ALTER TABLE jobs ADD COLUMN skills TEXT;")
        conn.commit()


def normalize_skills(skills):
    """
    Convert skills data into a comma-separated string.
    """
    if isinstance(skills, list):
        return ", ".join(skills)

    if skills is None:
        return ""

    try:
        if pd.isna(skills):
            return ""
    except TypeError:
        pass

    return str(skills)


def insert_job(conn, job):
    """
    Insert or update one job in the jobs table.
    """
    insert_sql = """
    INSERT INTO jobs (
        title,
        company,
        location,
        description,
        apply_url,
        source,
        skills
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(apply_url) DO UPDATE SET
        title = excluded.title,
        company = excluded.company,
        location = excluded.location,
        description = excluded.description,
        source = excluded.source,
        skills = excluded.skills;
    """

    conn.execute(
        insert_sql,
        (
            job.get("title", ""),
            job.get("company", ""),
            job.get("location", ""),
            job.get("description", ""),
            job.get("apply_url", None),
            job.get("source", ""),
            normalize_skills(job.get("skills", "")),
        ),
    )


def save_jobs_to_database(df, db_path=DB_PATH):
    """
    Save all jobs from a DataFrame into the SQLite database.
    """
    conn = create_connection(db_path)
    create_jobs_table(conn)
    migrate_jobs_table(conn)

    for _, job in df.iterrows():
        insert_job(conn, job)

    conn.commit()
    conn.close()


def load_jobs_from_database(db_path=DB_PATH):
    """
    Load all jobs from the SQLite database into a DataFrame.
    """
    conn = create_connection(db_path)
    create_jobs_table(conn)
    migrate_jobs_table(conn)

    query = """
    SELECT
        id,
        title,
        company,
        location,
        description,
        apply_url,
        source,
        skills
    FROM jobs
    ORDER BY id;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df