import os
import logging
from send_email import send_alert

# === Setup Logging ===
log_file = "etl.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_step(script_name):
    logging.info(f"Running: {script_name}")
    result = os.system(f"python {script_name}")
    if result != 0:
        raise RuntimeError(f"{script_name} failed with exit code {result}")
    logging.info(f"Finished: {script_name}")

try:
    logging.info("=== START: Crypto ETL Pipeline ===")
    run_step("scripts/extract.py")
    run_step("scripts/transform.py")
    run_step("scripts/load.py")
    logging.info("=== SUCCESS: Pipeline completed ===")

    # Send success email
    send_alert("✅ Crypto ETL Completed",
               "Your crypto ETL pipeline ran successfully.\n\nCheck the log file: etl.log")

except Exception as e:
    logging.error("❌ ETL Failed", exc_info=True)

    # Get last 30 lines of log
    with open(log_file, "r") as f:
        logs = f.readlines()
        last_logs = "".join(logs[-30:])

    # Send failure email with logs
    send_alert("❌ Crypto ETL Failed",
               f"ETL failed with error:\n{e}\n\n--- Recent Logs ---\n{last_logs}")