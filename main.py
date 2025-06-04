import schedule
import time
from Fitbit_Fetch import *  # importing the script will run it once

# Their script runs everything at import; we keep the process alive
schedule.every(15).minutes.do(lambda: None)

while True:
    schedule.run_pending()
    time.sleep(60)
