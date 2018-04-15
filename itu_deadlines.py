import data_extraction
import calendar_adder
import getpass
import os
import json

home_dir = os.path.expanduser('~')
credential_dir = os.path.join(home_dir, '.credentials')
ems_ps_file = credential_dir + "/ems_ps.json"

if not os.path.isfile(ems_ps_file):
    user_name = raw_input("Enter your ems user name:\n")
    password = getpass.getpass("Enter your login password:\n")
    data = data_extraction.login(user_name, password)
    data_extraction.write_to_file(data)
    ps = {
        'user': user_name,
        'ps': password
    }
    with open(ems_ps_file, 'w') as f:
        json.dump(ps, f)
else:
    use_local = raw_input("Do you want to use existing credential? at {} (y/n)\n".format(ems_ps_file))
    if use_local.lower() == 'n':
        user_name = raw_input("Enter your ems user name:\n")
        password = getpass.getpass("Enter your login password:\n")
        data = data_extraction.login(user_name, password)
        data_extraction.write_to_file(data)
        ps = {
            'user': user_name,
            'ps': password
        }
        with open(ems_ps_file, 'w') as f:
            json.dump(ps, f)
    else:
        with open(ems_ps_file, 'r') as f:
            ps = json.load(f)
            user_name = ps['user']
            password = ps['ps']
        data = data_extraction.login(user_name, password)
        data_extraction.write_to_file(data)

calendar_adder.add_deadline()