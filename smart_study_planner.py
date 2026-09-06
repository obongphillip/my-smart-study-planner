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

def search_by_subject(subject):
    matches = []

    for record in sessions:
        recorded_subject = record["subject"].casefold()
        requested_subject = subject.casefold()

        if recorded_subject == requested_subject:
            matches.append(record)

    print(f"\n[ SEARCH RESULTS FOR: {subject.upper()} ]")

    if not matches:
        print("No study sessions were recorded for that subject.")
        return

    total_minutes = 0

    for number, record in enumerate(matches, start=1):
        total_minutes += record["duration"]
        session_type = classify_session(record["duration"])

        print(
            f"{number}. {record['topic']} | "
            f"{record['date']} | "
            f"{record['duration']:g} minutes | "
            f"{session_type}"
        )

    total_hours = total_minutes / 60

    print(f"\nMatching sessions: {len(matches)}")
    print(f"Total subject time: {total_minutes:g} minutes")
    print(f"Equivalent time: {total_hours:.2f} hours")

def study_statistics():
    print("\n[ STUDY PROGRESS SUMMARY ]")

    if not sessions:
        print("Statistics cannot be calculated because no sessions exist.")
        return

    subject_minutes = {}
    subject_labels = {}
    overall_minutes = 0

    for record in sessions:
        subject_key = record["subject"].casefold()

        subject_labels.setdefault(
            subject_key,
            record["subject"].title()
        )

        subject_minutes[subject_key] = (
            subject_minutes.get(subject_key, 0)
            + record["duration"]
        )

        overall_minutes += record["duration"]

    weakest_subject = min(
        subject_minutes,
        key=subject_minutes.get
    )

    longest_session = max(
        sessions,
        key=lambda record: record["duration"]
    )

    print(f"Overall study time: {overall_minutes / 60:.2f} hours")
    print("\nTime studied per subject:")

    for subject_key, minutes in subject_minutes.items():
        subject_name = subject_labels[subject_key]
        print(f"- {subject_name}: {minutes / 60:.2f} hours")

    print(
        f"\nWeakest area: {subject_labels[weakest_subject]} "
        f"({subject_minutes[weakest_subject] / 60:.2f} hours)"
    )

    print(
        f"Longest session: {longest_session['subject']} - "
        f"{longest_session['topic']} "
        f"({longest_session['duration']:g} minutes)"
    )
