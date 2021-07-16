#import requests
import icalendar
import recurring_ical_events
from pathlib import Path
from datetime import date, datetime, timedelta
from dateutil import parser
import pytz
import json

# local test
result = Path('wilco.ics').read_text()
#result = requests.get('https://calendar.google.com/calendar/ical/opqodcvmhut1cmloulh8ajdb8k%40group.calendar.google.com/private-753ba38272a9f23f41806213f9867fba/basic.ics')
cal = icalendar.Calendar.from_ical(result)


# to search upcoming events, we'll query between now and the next several days
todatetime = datetime.now().astimezone(pytz.timezone('US/Pacific'))
todate = date.today()
two_days = todate + timedelta(days=3)
today = todate.strftime('%Y-%m-%d')
start_date_tuple = (int(todate.strftime('%Y')), int(todate.strftime('%m')), int(todate.strftime('%d')))
end_date_tuple = (int(two_days.strftime('%Y')), int(two_days.strftime('%m')), int(two_days.strftime('%d')))

events = recurring_ical_events.of(cal).between(start_date_tuple, end_date_tuple)
event_list = []
for event in events:
    temp = event.get('dtstart').dt
    if isinstance(temp, datetime):
        dtstart = temp.astimezone(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d")
        event_time = temp.astimezone(pytz.timezone('US/Pacific'))
        event_time_epoch = event_time.strftime('%s')
    else:
        dtstart = temp.strftime("%Y-%m-%d")
    current_event = {'summary': str(event['SUMMARY']), 'event_time': event_time, 'datetime': event_time_epoch}
    event_list.append(current_event)
event_list.sort(key=lambda x: x.get('datetime'))
is_next_event = False
for event in event_list:
    if (todatetime < event['event_time']):
        next_event = {'summary': event['summary'], 'time': event['event_time'].strftime('%-H:%M%p')}
        is_next_event = True
        break
if is_next_event:
    print (next_event['summary'], next_event['time'])
else:
    print ('no upcoming events')
