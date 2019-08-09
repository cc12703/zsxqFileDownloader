

from selenium import webdriver
import logging



logger = logging.getLogger(__name__)

custom_isLoad = False
custom_useragent = None
custom_accessToken = None



class RequestCustomHeaderMiddleware(object) :


    def __loadCustomInfo(self) :
        global custom_isLoad
        global custom_useragent
        global custom_accessToken

        if custom_isLoad :
            return
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('disable-infobars')
        options.add_argument('--user-data-dir=./chrome-user-data')
        driver = webdriver.Chrome(chrome_options=options)

        driver.get('https://wx.zsxq.com')

        custom_accessToken = driver.get_cookie('zsxq_access_token')['value']
        logger.info('use accessToken is %s', custom_accessToken)

        custom_useragent = driver.execute_script("return navigator.userAgent;").replace('HeadlessChrome', 'Chrome')
        logger.info('use user-agent is %s', custom_useragent)

        custom_isLoad = True

        driver.close()

    def process_request(self, request, spider):
        global custom_useragent
        global custom_accessToken

        self.__loadCustomInfo()

        request.headers.setdefault('User-Agent', custom_useragent)        
        request.headers.setdefault('Cookie', "zsxq_access_token={0}".format(custom_accessToken))

