import time
from datetime import datetime as dt

hosts_temp = "hosts" #テスト用のホスト
hosts_path = "/etc/hosts" #実際のホストパス
redirect = "127.0.0.1" #localhost
website_list = ["https://twitter.com", "twitter.com", "https://www.youtube.com", "youtube.com"]
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
			content = file.readlines()#readlinesでカーソル文末に移動してる
			file.seek(0)#カーソル戻す
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)#website_listがある文は書き込みしない
			file.truncate()
		print("Fun hours...")
	time.sleep(5)
#書き込みはcronにさせる
