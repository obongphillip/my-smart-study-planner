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

