

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def prepare_browser():
    chrome_options = Options()

    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    '''
    chrome_options.add_argument(
        'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    '''
    #注释这句就是不使用无头浏览器
    chrome_options.add_argument('--headless')
    capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
    capabilities['acceptSslCerts'] = True
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
