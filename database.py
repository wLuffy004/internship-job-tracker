import sqlite3
import pandas as pd


DB_PATH = "data/jobs.db"


def create_connection(db_path=DB_PATH):
    """
    Create a connection to the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    return conn


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
        source TEXT
    );
    """

    conn.execute(create_table_sql)
    conn.commit()


def insert_job(conn, job):
    """
    Insert one job into the jobs table.
    If the apply_url already exists, ignore the duplicate.
    """
    insert_sql = """
    INSERT OR IGNORE INTO jobs (
        title,
        company,
        location,
        description,
        apply_url,
        source
    )
    VALUES (?, ?, ?, ?, ?, ?);
    """

    conn.execute(
        insert_sql,
        (
            job["title"],
            job["company"],
            job["location"],
            job["description"],
            job["apply_url"],
            job["source"],
        ),
    )


def save_jobs_to_database(df, db_path=DB_PATH):
    """
    Save all jobs from a DataFrame into the SQLite database.
    """
    conn = create_connection(db_path)
    create_jobs_table(conn)

    for _, job in df.iterrows():
        insert_job(conn, job)

    conn.commit()
    conn.close()


def load_jobs_from_database(db_path=DB_PATH):
    """
    Load all jobs from the SQLite database into a DataFrame.
    """
    conn = create_connection(db_path)

    query = """
    SELECT
        title,
        company,
        location,
        description,
        apply_url,
        source
    FROM jobs
    ORDER BY id;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df
