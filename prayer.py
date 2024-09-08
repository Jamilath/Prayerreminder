import requests
import schedule
import time
from datetime import datetime
from plyer import notification

# Function to fetch prayer times from Aladhan API
def get_prayer_times():
    # Replace with your actual city and country or use coordinates
    city = "Hyderabad"
    country = "India"
    response = requests.get(f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2")
    data = response.json()
    return data['data']['timings']

# Function to send notification
def notify(prayer_name):
    notification.notify(
        title=f"Time for {prayer_name} Prayer",
        message="Please stop other things and pray.",
        timeout=10
    )

# Schedule notifications
def schedule_notifications():
    prayer_times = get_prayer_times()
    for prayer, time_str in prayer_times.items():
        prayer_time = datetime.strptime(time_str, "%H:%M").time()
        schedule.every().day.at(prayer_time.strftime("%H:%M")).do(notify, prayer)

# Run the scheduler
def run_scheduler():
    schedule_notifications()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()