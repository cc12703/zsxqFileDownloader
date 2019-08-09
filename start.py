

from selenium import webdriver
import time
import sys
import datetime
import os
import logging


logger = logging.getLogger(__name__)


def __login() :
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('--user-data-dir=./chrome-user-data')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://wx.zsxq.com')
    token = driver.get_cookie('zsxq_access_token')
    while token == None :
        time.sleep(5)
        token = driver.get_cookie('zsxq_access_token')


    logger.info('token is %s', driver.get_cookie('zsxq_access_token'))
    logger.info('user agent is %s', driver.execute_script("return navigator.userAgent;"))

    driver.close()


def __checkTokenValid() :
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('disable-infobars')
    options.add_argument('--user-data-dir=./chrome-user-data')
    driver = webdriver.Chrome(options=options)

    driver.get('https://wx.zsxq.com')
    token = driver.get_cookie('zsxq_access_token')
    driver.close()

    if token == None :
        return False

    expiryDate = datetime.datetime.utcfromtimestamp(token['expiry'])
    curDate = datetime.datetime.utcnow()
    if expiryDate <= curDate :
        return False

    return True




def main(argv) :
    if not __checkTokenValid() :
        __login()

    os.system('scrapy crawl zsxq')





if __name__ == "__main__" :
    main(sys.argv[1:])