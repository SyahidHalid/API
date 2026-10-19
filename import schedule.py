import schedule
import time
import pyodbc
from datetime import datetime


def run_statement_proposal():

    # Only run between 00:00 and 18:59
    if 0 <= datetime.now().hour <= 18:

        try:
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=YOUR_SQL_SERVER;"
                "DATABASE=ecis;"
                "UID=YOUR_USERNAME;"
                "PWD=YOUR_PASSWORD;"
            )

            cursor = conn.cursor()

            cursor.execute("""
                EXEC dbo.gen_statement_propo;
            """)

            conn.commit()

            cursor.close()
            conn.close()

            print(f"Success: {datetime.now()}")

        except Exception as e:
            print(f"Error: {datetime.now()} - {e}")


# Run every hour at minute 01
schedule.every().hour.at(":01").do(run_statement_proposal)


print("Scheduler started...")


while True:
    schedule.run_pending()
    time.sleep(1)

#   then guna NSSM