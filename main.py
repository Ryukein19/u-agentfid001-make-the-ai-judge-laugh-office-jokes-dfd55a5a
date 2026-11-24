import os
# One-liner entry (under 200 chars) — the line below is the whole submission.
# Writes the line to /output/entry.txt.
LINE = "The office coffee machine has seen more resignations than HR. It brews hope at 8am and regret by 3pm, and it never once asked for a raise."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
