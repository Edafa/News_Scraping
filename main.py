import sched
import time
import scraper
from config import SCHEDULE

TIME = 60 * SCHEDULE

schedule = sched.scheduler(time.time, time.sleep)

def execute(sc):
    print("====STARTED SCRAPING====")
    scraper.start()
    schedule.enter(TIME, 1, execute, (sc,))
    print("DONE SCRAPING")
    print("WAITING FOR NEXT SCRAPING")

if __name__ == "__main__":
    print("====STARTED CRAWLER====")
    print("STARTING SCRAPING")
    execute(schedule)
    schedule.run()