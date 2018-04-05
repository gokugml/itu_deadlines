import json
import os
import pprint
import re
import time

pp = pprint.PrettyPrinter(indent=4)

class DataParser(object):
    def __init__(self):

        return

    def json_to_dict(self, file):
        if os.path.isfile(file):
            with open(file, 'r') as f:
                dict = json.load(f)
                return dict

    def time_to_event_time(self, ems_time):
        """2018-04-1T09:00:00-07:00"""
        month_map = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
        }
        # # year = time[1].strip()
        # match_year = re.search('(20[0-9][0-9])', ems_time)
        # if match_year:
        #     year = match_year.group(1)
        # match = re.search('(...) (\d+) (\d+):(\d+) (AM|PM)', ems_time)
        # # match = re.search('(...) (\d+) (\d+):(\d+) (AM|PM)(, (\d+))?') # with year
        # if match:
        #     month = match.group(1)
        #     date = match.group(2)
        #     hour = match.group(3)
        #     min = match.group(4)
        #     am_pm = match.group(5)
        time_tuple = time.strptime(ems_time, '%b %d %I:%M %p') # Feb 3 4:00 PM
        print time_tuple
        print time_tuple.tm_mon
        print time_tuple.tm_mday
        print time_tuple.tm_hour
        print time_tuple.tm_min
        print time.strftime('%b %d %I:%M %p', time_tuple)
        #
        # if end != 0:
        #     calendar_time = "{}-{}-{}T10:00:00-07:00".format(year, month_map[month], date)
        # else:
        #     calendar_time = "{}-{}-{}T09:00:00-07:00".format(year, month_map[month], date)
        # print calendar_time
        # return calendar_time

    def _get_month(self, ):
        return




if __name__ == "__main__":
    test = DataParser()
    path = os.path.dirname(__file__)+"/data.json"
    dict = test.json_to_dict(path)
    # pp.pprint(dict)
    for key, dict_time in dict.items():
        test.time_to_event_time(dict_time['Due'])

