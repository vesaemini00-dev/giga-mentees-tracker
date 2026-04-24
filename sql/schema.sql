CREATE TABLE IF NOT EXISTS mentees (
    id          SERIAL PRIMARY KEY,
    full_name   VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    cohort      VARCHAR(20)  NOT NULL,
    enrolled_on DATE         DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS assessments (
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS scores (
    id            SERIAL PRIMARY KEY,
    assessment_id INT NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
    email         VARCHAR(100) NOT NULL,
    score         INT NOT NULL CHECK (score >= 0 AND score <= 100)
);