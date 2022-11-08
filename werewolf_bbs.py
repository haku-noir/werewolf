from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import time
import pandas as pd

CHROME_DRIVER = '/opt/chrome/chromedriver'

def save_messages(vid_min, vid_max):
  options = Options()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')

  chrome_service = fs.Service(executable_path=CHROME_DRIVER) 
  driver = webdriver.Chrome(service=chrome_service, options=options)

  for i in range(vid_min, vid_max+1):
    names = []
    messages = []
    days = []
    ranges = []
    announces = []
    print(str(i)+"/"+str(vid_max), end=" ")
    for j in range(20):
      print(j, end=" ")
      URL = 'http://ninjinix.x0.com/wolf0/index.rb?vid=' + str(i) + '&meslog=' + str(i) + '_progress_'+ str(j) + '&mode=say'

      driver.get(URL)
      time.sleep(1)

      tags = driver.find_elements(by=By.CSS_SELECTOR, value=".message > a")
      if len(tags) == 0:
        break
      for tag in tags:
        names.append(tag.text)

      tags = driver.find_elements(by=By.CSS_SELECTOR, value=".mes_say_body1")
      for tag in tags:
        messages.append(tag.text)

      days.append(j)
      ranges.append(len(names))

      tags = driver.find_elements(by=By.CSS_SELECTOR, value="div.announce")
      announce = ""
      for tag in tags:
        announce += tag.text
      announces.append(announce)

    print("finished")

    dict = {'name': names, 'message': messages}
    df = pd.DataFrame(dict)
    df.to_csv('output/werewolf_bbs_messages_'+str(i)+'.csv',encoding='cp932')

    dict = {'day': days, 'range': ranges, 'announce': announces}
    df = pd.DataFrame(dict)
    df.to_csv('output/werewolf_bbs_day_info_'+str(i)+'.csv',encoding='cp932')

if __name__ == '__main__':
  VID_MIN = 100
  VID_MAX = 111
  save_messages(VID_MIN, VID_MAX)
