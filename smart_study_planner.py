sessions = []

SHORT_LIMIT = 30
MEDIUM_LIMIT = 90


def classify_session(duration):
    if duration > MEDIUM_LIMIT:
        return "Long"
    elif duration >= SHORT_LIMIT:
        return "Medium"
    else:
        return "Short"

def read_positive_minutes():
    while True:
        entry = input("Study duration in minutes: ").strip()

        try:
            minutes = float(entry)

            if minutes <= 0:
                print("Duration must be more than zero.")
                continue

            return minutes

        except ValueError:
            print("Please enter the duration using numbers only.")

def add_session():
    print("\n[ RECORD A STUDY SESSION ]")

    subject_name = input("Subject studied: ").strip()
    topic_name = input("Topic covered: ").strip()
    study_day = input("Date or day label: ").strip()
    minutes = read_positive_minutes()

    new_record = {
        "subject": subject_name,
        "topic": topic_name,
        "date": study_day,
        "duration": minutes
    }

    sessions.append(new_record)

    session_type = classify_session(minutes)

    print(f"Session recorded successfully as {session_type}.")

def view_sessions():
    print("\n[ ALL RECORDED STUDY SESSIONS ]")

    if len(sessions) == 0:
        print("There are currently no study sessions to display.")
        return

    line = "=" * 102

    print(line)
    print(
        f"{'ID':<5} | "
        f"{'SUBJECT':<28} | "
        f"{'TOPIC':<24} | "
        f"{'DATE/DAY':<14} | "
        f"{'MINUTES':<8} | "
        f"{'TYPE':<8}"
    )
    print(line)

        for position, record in enumerate(sessions, start=1):
        session_type = classify_session(record["duration"])

        print(
            f"{position:<5} | "
            f"{record['subject']:<28} | "
            f"{record['topic']:<24} | "
            f"{record['date']:<14} | "
            f"{record['duration']:<8g} | "
            f"{session_type:<8}"
        )

