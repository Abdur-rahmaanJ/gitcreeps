import json

import maya


days = {
    0:'monday',
    1:'tuesday',
    2:'wednesday',
    3:'thursday',
    4:'friday',
    5:'saturday',
    6:'sunday'
}

NEWLINE = '\n'
SPACE = ' '
COLON = ':'

def day(t):

    # where t means unformatted time
    maya_datetime = maya.parse(t).datetime()
    weekday = maya_datetime.weekday()
    try:
        return days[weekday]
    except KeyError:
        return None

def hour(t):

    maya_datetime = maya.parse(t).datetime()
    hour = maya_datetime.hour
    return hour

def date(t):

    maya_datetime = maya.parse(t).datetime()
    date = maya_datetime.date()
    return date


def empty_name_data():
    '''
    {
        'monday': {
            'commits':0,
            'times':[]
        },
        'tuesday': {
         ...
    }
    '''

    data = {}
    for key in days:
        day = days[key]
        data[day] = {
            'commits':0,
            'times':[]
        }
    return data


def to_json_file(data, filename):

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def parse_log(file_name):
    '''
    using command: git shortlog --format=format:%cI
    produces data in the format:

    {
        'name':[
            'TIMEZONEDATA',
            'TIMEZONEDATA'
        ],
        'name2':[

        ]
    }
    '''

    raw_data = {}
    current_name = None

    with open(file_name) as f:
        source = f.read()

    lines = source.split(NEWLINE)

    for line in lines:
        if line:
            if line[0] != SPACE:
                name = SPACE.join(line.strip(COLON).split(SPACE)[:-1])
                current_name = name
                raw_data[current_name] = []
            elif line[0] == SPACE:
                raw_data[current_name].append(line.strip())
        else:
            current_name = None

    return raw_data

def get_clean_data(logfilename):
    '''
    produces data in the format:

    "Abdur-Rahmaan Janhangeer": {
        "monday": {
            "commits": 19,
            "times": [
                "2019-03-11@06:42:39",
                "2019-03-25@02:59:00"
            ]
        },
        "tuesday": {
        ...
    }
    '''

    log_data = parse_log(logfilename)
    clean_data = {}

    for name in log_data:
        clean_data[name] = empty_name_data()

        unformatted_times = log_data[name]
        for t in unformatted_times:
            dayoftheweek = day(t)
            clean_data[name][dayoftheweek]['commits'] += 1
            #commit_time = str(maya_datetime.time())
            #commit_date = str(maya_datetime.date())
            clean_data[name][dayoftheweek]['times'].append(t)
    
    return clean_data


def merge_names(clean_data, namelist, default=None):
    default_name = default
    data = empty_name_data()
    for name in namelist:
        for day in days:
            wday = days[day]
            data[wday]['commits'] += clean_data[name][wday]['commits']
            data[wday]['times'] += clean_data[name][wday]['times']

    for name in namelist:
        if name == default:
            continue
        del clean_data[name] 

    clean_data[default_name] = data

