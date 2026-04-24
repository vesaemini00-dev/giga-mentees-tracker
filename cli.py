import argparse
from queries import (
    create_mentee,
    list_mentees,
    update_mentee,
    delete_mentee,
    create_assessment_with_scores
)

def run_cli():
    parser = argparse.ArgumentParser(description="GigaAcademy CLI")

    subparsers = parser.add_subparsers(dest="command")

    # MENTEE
    mentee_parser = subparsers.add_parser("mentee")
    mentee_sub = mentee_parser.add_subparsers(dest="action")

    add = mentee_sub.add_parser("add")
    add.add_argument("--name", required=True)
    add.add_argument("--email", required=True)
    add.add_argument("--cohort", required=True)

    mentee_sub.add_parser("list")

    update = mentee_sub.add_parser("update")
    update.add_argument("--id", type=int, required=True)
    update.add_argument("--cohort", required=True)

    delete = mentee_sub.add_parser("delete")
    delete.add_argument("--id", type=int, required=True)

    # ASSESSMENT
    assess_parser = subparsers.add_parser("assessment")
    assess_sub = assess_parser.add_subparsers(dest="action")

    create = assess_sub.add_parser("create")
    create.add_argument("--title", required=True)
    create.add_argument("--scores", required=True)

    args = parser.parse_args()

    if args.command == "mentee":

        if args.action == "add":
            mentee_id = create_mentee(args.name, args.email, args.cohort)
            print(f"✅ Mentee added with id: {mentee_id}")

        elif args.action == "list":
            mentees = list_mentees()
            for m in mentees:
                print(m)

        elif args.action == "update":
            updated = update_mentee(args.id, args.cohort)
            print("✅ Updated" if updated else "❌ Not found")

        elif args.action == "delete":
            deleted = delete_mentee(args.id)
            print("✅ Deleted" if deleted else "❌ Not found")

    elif args.command == "assessment":

        if args.action == "create":
            pairs = args.scores.split(",")
            scores_dict = {}

            for p in pairs:
                email, score = p.split(":")
                scores_dict[email.strip()] = int(score.strip())

            assessment_id = create_assessment_with_scores(
                args.title, scores_dict
            )

            print(f"✅ Assessment created with id: {assessment_id}")