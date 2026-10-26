
import csv
import os
from datetime import datetime


LOG_FILE = "data/activity_log.csv"


def log_activity(state, filename, timestamp=None):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    if timestamp is None:
        timestamp = datetime.now()

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(LOG_FILE) == 0:
            writer.writerow(["timestamp", "state", "filename"])

        writer.writerow([
            timestamp.isoformat(timespec="seconds"),
            state,
            filename,
        ])
