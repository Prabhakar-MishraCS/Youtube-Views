
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback
import random
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)

print("\nProcess Started\n")

try:
    videos = [
        'https://youtu.be/qmZiwfv7KrU',
        'https://youtu.be/C2VT_BUN5WI',
        'https://youtu.be/028BYBiPZ9E',
        'https://youtu.be/ca6mirL0kVM',
        'https://youtu.be/GNe91BgX4FU',
        'https://youtu.be/qSHMLYN1e5A'
    ]

    for i in range(10):
        print("Watching for {} time".format(i+1))
        choose_video = random.randint(0, 5)
        driver.get(videos[choose_video])
        #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        sleep_time = random.randint(5, 10)
        time.sleep(sleep_time)  # Let the user actually see something


except:
    print(traceback.format_exc())
finally:
    driver.quit()
