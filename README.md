# GigaAcademy Mentees Tracker

This is a Python application for managing mentees using a PostgreSQL database.
It includes both a CLI (command line interface) and a FastAPI backend.

## Features

- Add, list, update, and delete mentees
- Command-line interface (CLI) using argparse
- PostgreSQL database connection
- Docker for database setup
- Transactions (assessment + scores)
- FastAPI API with interactive docs

## Setup

```bash
cp .env.example .env
docker compose up -d

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## How to Run

### CLI

```bash
python3 app.py mentee add --name "Vesa" --email "vesa@test.com" --cohort "2026"
python3 app.py mentee list

## Level Completed

✔ Level 1  
✔ Level 2  

- CRUD operations implemented  
- File structure split (db.py, queries.py, cli.py, app.py)  
- Transactions (assessment + scores)  
- CLI using argparse  
- FastAPI API included  

## What Was Challenging

The most challenging part was setting up the PostgreSQL connection and making sure the environment variables matched the Docker configuration.  
I initially faced issues with database authentication and had to reset the Docker volume to fix it.  
Understanding how argparse works with subcommands was also new and required careful structuring.  
Additionally, working with FastAPI was challenging since I had just started learning it, but it helped me understand how to build and expose API endpoints.  
Overall, integrating the CLI, database, and API together helped me better understand how backend systems work.