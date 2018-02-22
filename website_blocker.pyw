import time
from datetime import datetime as dt
host2="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_lists=["www.facebook.com","facebok.com","www.youtube.com","youtube.com"]

while True:
  if dt(dt.now().year,dt.now().month,dt.now().day,18)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23,50):
      print("Working hours")
      with open(hosts_path,'r+') as file:
          content=file.read()
          for website in website_lists:
              if website in content:
                pass
              else:
                file.write(redirect+" "+website+"\n")
  else:
      with open(hosts_path,'r+') as file:
          content=file.readlines()
          file.seek(0)
          for line in content:
              if not any(website in line for website in website_lists):
                  file.write(line)
          file.truncate()
      print("fun hours")
  time.sleep(5)
