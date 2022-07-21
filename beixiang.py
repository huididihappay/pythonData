from common.prepare import prepare_browser
from time import sleep
from models.jijin import Beixiang
from mysql_data import createAll
from datetime import datetime

urls = ['https://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sz',
            'https://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh']

def start_beixiang():

    browser = prepare_browser()
    sleep(0.5)
    date_string = '11-05-2021'
    date_object = datetime.strptime(date_string, '%d-%m-%Y')
    for url in urls:
        objs = []
        browser.get(url)
        while browser.current_url.find("hkexnews") == -1:
            sleep(0.2)
        tbody = browser.find_element_by_xpath('//*[@id="mutualmarket-result"]/tbody')
        trlist = tbody.find_elements_by_tag_name("tr")
        for row in trlist:
            tdlist = row.find_elements_by_tag_name("td")
            code = conver_code(tdlist[0].text)
            name = code_name(code,tdlist[1].text)
            num = int(tdlist[2].text.replace(',',''))
            scale = float(tdlist[3].text[:-1])
            o = Beixiang(code,name,num,scale,date_object)
            objs.append(o)
        createAll(objs)



def conver_code(code):
    if code.startswith("70"):
        return "000"+code[2:]
    elif code.startswith("72"):
        return "00"+code[1:]
    elif code.startswith("77"):
        return "300"+code[2:]
    elif code.startswith("30"):
        return "688"+code[2:]
    elif code.startswith("9"):
        return "60"+code[1:]
    return code

def code_name(code,name):
    if code == "300119":
        return "瑞普生物"
    if code == "600346":
        return "片仔徨"
    return name

if __name__ == "__main__":
    start_beixiang()
    # date_string = '09-05-2021'
    # date_object = datetime.strptime(date_string, '%d-%m-%Y')
    # objs = []
    # o = Beixiang('000001', '平安銀行', 2187779221, 11.27, date_object)
    # objs.append(o)
    # createAll(objs)
