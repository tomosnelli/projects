"""
Name: tomosnelli
Last modified: May 8 2021
"""

import time
from datetime import datetime as dt


def HOSTS_TEST():
    return "test"  # a test for our hosts file


def HOSTS_PATH():
    return "/etc/hosts" # the actual path that will be used for implementing blocker


def LOCALHOST():
    return "127.0.0.1" #localhost


def WEBSITE_LIST():
    return ["https://twitter.com", "twitter.com", "https://www.youtube.com", "youtube.com"]


def HOUR_NOW():
    return dt.now().hour


def work_hour():
    return 9 <= HOUR_NOW() <= 16


def write_website_to_file():
    with open(HOSTS_TEST(), 'r+') as file_object:
        blocked_list_file = file_object.read()
        for website in WEBSITE_LIST():
            if website not in blocked_list_file:
                file_object.write(LOCALHOST() + " " + website + "\n")
                # work hours. dont be looking at youtube


def remove_links_from_file():
    with open(HOSTS_TEST(), 'r+') as file_object:
        content = file_object.readlines()
        file_object.seek(0)
        for line in content:
            if not any(website in line for website in WEBSITE_LIST()):
                file_object.write(line)
        file_object.truncate()


def block():
    """block specified website if hour of day is between 9 and 16.

    :postcondition: rewrite the file test or /etc/hosts if hour of day is between 9 and 17
                    else delete blocked websites in test.txt
    :return: None
    """
    while True:
        if work_hour(): 
            write_website_to_file()
            # write into /etc/hosts redirect to localhost when access WEBSITE_LIST links
            print("Work Hours")
        else:
            remove_links_from_file()
            print("Off Duty!")
        time.sleep(5)


def main():
    block()


if __name__ == "__main__":
    main()

