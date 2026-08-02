from datetime import datetime
import os

LOG_FILE = "logs/log.txt"

def save_log(prompt, analysis, refined_prompt, response, execution_time):

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 80 + "\n")
        file.write(f"Timestamp      : {datetime.now()}\n")
        file.write("-" * 80 + "\n")

        file.write(f"Original Prompt:\n{prompt}\n\n")

        file.write(f"Prompt Category:\n{analysis}\n\n")

        file.write(f"Refined Prompt:\n{refined_prompt}\n\n")

        file.write(f"Final Response:\n{response}\n\n")

        file.write(f"Execution Time : {execution_time} seconds\n")

        file.write("=" * 80 + "\n\n")