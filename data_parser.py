import json
import os
import pprint
import re
import time

pp = pprint.PrettyPrinter(indent=4)

class DataParser(object): #  TODO: support time zone converter
    def __init__(self):
        return

    def json_to_dict(self, file):
        if os.path.isfile(file):
            with open(file, 'r') as f:
                dict = json.load(f)
                return dict

    def gen_event(self, dict=None):
        available_tuple = self.convert_tuple(dict['Available'])
        due_tuple = self.convert_tuple(dict['Due'])
        # print(dict['Available'], available_tuple)
        # print(dict['Due'], due_tuple)

        available_time = time.mktime(available_tuple)
        due_time = time.mktime(due_tuple)

        delta_time = due_time - available_time
        if delta_time > 86400:
            available_start = available_time
            available_end = available_time + 3600
            due_start = due_time - 3600
            due_end = due_time
            event_available = {
                'summary': 'Available: ' + dict['Title'],
                'location': '2711 N 1st St, San Jose, CA 95134',
                'description': dict['Available'],
                'start': {
                    'dateTime': self.sec_to_google_time(available_start),
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': self.sec_to_google_time(available_end),
                    'timeZone': 'America/Los_Angeles',
                }
            }
            event_due = {
                'summary': 'Due: ' + dict['Title'],
                'location': '2711 N 1st St, San Jose, CA 95134',
                'description': dict['Due'],
                'start': {
                    'dateTime': self.sec_to_google_time(due_start),
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': self.sec_to_google_time(due_end),
                    'timeZone': 'America/Los_Angeles',
                }
            }
            return [event_available, event_due]
        else:
            start = available_time
            end = due_time
            event = {
                'summary': dict['Title'],
                'location': '2711 N 1st St, San Jose, CA 95134',
                'description': dict['Available'] + ' to ' + dict['Due'],
                'start': {
                    'dateTime': self.sec_to_google_time(start),
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': self.sec_to_google_time(end),
                    'timeZone': 'America/Los_Angeles',
                }
            }
            return [event]

    def convert_tuple(self, time_in):
        """2018-04-1T09:00:00-07:00"""
        match = re.search(',\s?([1-9][0-9][0-9][0-9])', time_in)
        if not match:
            time_in = "{}, {}".format(time_in, time.strftime('%Y', time.localtime())) # Feb 3 4:00 PM
        time_tuple = time.strptime(time_in, '%b %d %I:%M %p, %Y')
        return time_tuple

    def sec_to_google_time(self, sec):
        tuple = time.localtime(sec)
        # print(tuple)
        calendar_time = time.strftime("%Y-%m-%dT%H:%M:%S-07:00", tuple)
        return calendar_time


if __name__ == "__main__":
    path = os.path.dirname(__file__)+"/data.json"
    test = DataParser()
    data = test.json_to_dict(path)
    pp.pprint(data)
    # print test.convert_tuple('Feb 3 4:00 PM')
    # print test.convert_tuple('Feb 3 12:00 AM')
    # print test.convert_tuple('Feb 3 01:00 AM')
    # print test.convert_tuple('Feb 3 4:00 PM, 2000')
    # for key, item in data.items():
    #     events = test.gen_event(item)
    #     pp.pprint(events)
