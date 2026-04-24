import psycopg
import psycopg.errors
from db import get_connection


def create_mentee(full_name: str, email: str, cohort: str) -> int:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO mentees (full_name, email, cohort)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                """, (full_name, email, cohort))
                return cur.fetchone()[0]

    except psycopg.errors.UniqueViolation:
        raise ValueError(f"A mentee with email '{email}' already exists.")


def list_mentees():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, full_name, email, cohort, enrolled_on
                FROM mentees
                ORDER BY full_name;
            """)
            return cur.fetchall()


def update_mentee(mentee_id: int, new_cohort: str) -> bool:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE mentees
                SET cohort = %s
                WHERE id = %s;
            """, (new_cohort, mentee_id))
            return cur.rowcount > 0


def delete_mentee(mentee_id: int) -> bool:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM mentees
                WHERE id = %s;
            """, (mentee_id,))
            return cur.rowcount > 0


# ============================
# TRANSACTIONS (Part B)
# ============================

def create_assessment_with_scores(title: str, scores_by_email: dict) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:

            # 1. krijo assessment
            cur.execute("""
                INSERT INTO assessments (title)
                VALUES (%s)
                RETURNING id;
            """, (title,))
            assessment_id = cur.fetchone()[0]

            # 2. shto scores
            for email, score in scores_by_email.items():
                cur.execute("""
                    INSERT INTO scores (assessment_id, email, score)
                    VALUES (%s, %s, %s);
                """, (assessment_id, email, score))

    return assessment_id