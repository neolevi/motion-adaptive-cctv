
import csv
import os
import sys
from collections import Counter
from datetime import datetime, date


LOG_FILE = "data/activity_log.csv"
REPORT_DIR = "reports"


def generate_daily_summary(target_date=None):
    if target_date is None:
        target_date = date.today()

    if not os.path.exists(LOG_FILE):
        print(f"No activity log found at: {LOG_FILE}")
        return

    records = []

    with open(LOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                timestamp = datetime.fromisoformat(row["timestamp"])
            except (ValueError, KeyError, TypeError):
                continue

            if timestamp.date() == target_date:
                records.append({
                    "timestamp": timestamp,
                    "state": row.get("state", "unknown"),
                    "filename": row.get("filename", ""),
                })

    if not records:
        print(f"No activity recorded for {target_date}.")
        return

    records.sort(key=lambda record: record["timestamp"])

    state_counts = Counter(record["state"] for record in records)
    first_time = records[0]["timestamp"]
    last_time = records[-1]["timestamp"]

    lines = [
        f"Daily CCTV Activity Summary — {target_date}",
        "=" * 45,
        f"Total recorded frames: {len(records)}",
        f"First recorded frame: {first_time:%H:%M:%S}",
        f"Last recorded frame:  {last_time:%H:%M:%S}",
        "",
        "Frames by motion state:",
    ]

    for state, count in sorted(state_counts.items()):
        lines.append(f"  {state}: {count}")

    lines.extend([
        "",
        "Recorded state timeline:",
    ])

    previous_state = None

    for record in records:
        if record["state"] != previous_state:
            lines.append(
                f"  {record['timestamp']:%H:%M:%S} — "
                f"{record['state']}"
            )
            previous_state = record["state"]

    lines.extend([
        "",
        "Note: Frame counts represent sampled images, not the",
        "total duration of motion or verified event durations.",
    ])

    report = "\n".join(lines)

    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(
        REPORT_DIR, f"daily_summary_{target_date}.txt"
    )

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report + "\n")

    print(report)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    requested_date = date.today()

    if len(sys.argv) > 1:
        try:
            requested_date = date.fromisoformat(sys.argv[1])
        except ValueError:
            print("Usage: python src\\daily_summary.py [YYYY-MM-DD]")
            raise SystemExit(1)

    generate_daily_summary(requested_date)
