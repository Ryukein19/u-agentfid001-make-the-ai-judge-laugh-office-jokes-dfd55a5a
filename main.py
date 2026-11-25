import os
# One-liner entry, 200 char cap: the line below is the whole submission.
# Writes the line out to /output/entry.txt.
LINE = "The office coffee machine has witnessed more resignations than HR — and it's never once asked for a raise."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
