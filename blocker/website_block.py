import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["https://twitter.com", "twitter.com", "www.po-kaki-to.com", "po-kaki-to.com", "https://www.youtube.com", "youtube.com"]
year = dt.now().year
month = dt.now().month
day = dt.now().day
now = dt.now()

while True:
	if dt(year, month, day, 9) < now < dt(year, month, day, 17): 
		with open(hosts_temp, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
		print("Work dumb cunt")
	else:
		with open(hosts_temp, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("Fun hours...")
	time.sleep(5)
