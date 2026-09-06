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

