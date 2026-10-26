# \# Motion-Adaptive CCTV Recording with Automated Daily Summarization

# 

# Records smarter, not just more: stores frames at a rate based on motion

# (active / idle / deep idle) and generates a timestamped daily summary.

# 

# \## Status

# Work in progress. Currently: motion detection and state machine.

# 

# \## Setup

# python -m venv venv

# venv\\Scripts\\activate

# pip install -r requirements.txt

# python src/motion\_state.py

# 

# \## Planned features

# \- Adaptive frame storage (4 fps idle / 1 fps deep idle)

# \- Metadata index (SQLite)

# \- Daily summary report

# \- Timeline dashboard

