import data_extraction
import calendar_adder
import getpass

user_name = raw_input("Enter your ems user name:\n")
password = getpass.getpass("Enter your login password:\n")

data_extraction.login(user_name, password)
calendar_adder.add_deadline()