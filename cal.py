#import requests
import icalendar
import recurring_ical_events
from pathlib import Path
from datetime import date, datetime, timedelta
from dateutil import parser
import pytz

# local test
result = Path('wilco.ics').read_text()
#result = requests.get('https://calendar.google.com/calendar/ical/opqodcvmhut1cmloulh8ajdb8k%40group.calendar.google.com/private-753ba38272a9f23f41806213f9867fba/basic.ics')
cal = icalendar.Calendar.from_ical(result)
todate = date.today()
two_days = todate + timedelta(days=2)
today = todate.strftime('%Y-%m-%d')
start_date_tuple = (int(todate.strftime('%Y')), int(todate.strftime('%m')), int(todate.strftime('%d')))
end_date_tuple = (int(two_days.strftime('%Y')), int(two_days.strftime('%m')), int(two_days.strftime('%d')))

events = recurring_ical_events.of(cal).between(start_date_tuple, end_date_tuple)
for event in events:
    temp = event.get('dtstart').dt
    if isinstance(temp, datetime):
        dtstart = temp.astimezone(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d")
        event_time = temp.astimezone(pytz.timezone('US/Pacific')).strftime("%I:%M%p")
    else:
        dtstart = temp.strftime("%Y-%m-%d")

    if dtstart == today:
        print (dtstart, event['SUMMARY'], event_time)

