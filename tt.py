
from common.prepare import prepare_browser
from time import sleep
from models.jijin import Jjjin,Gupiao
from mysql_data import createAll

url = "http://fund.eastmoney.com/trade/gp.html"
detail_url="http://fundf10.eastmoney.com/ccmx_{code}.html"
jj_url_str = "http://fund.eastmoney.com/{code}.html"
def start_tt():
    i =0
    browser = prepare_browser()
    sleep(0.5)
    browser.get(url)
    while browser.current_url.find("fund") == -1:
        sleep(0.2)
    while True:
        get_table(browser)
        page = browser.find_element_by_xpath('//*[contains(text(),"下一页")]')
        print(page.text+str(i+1))
        if page.get_attribute("class") == 'end':
            print('end')
            return
        browser.execute_script("arguments[0].click();", page)
        sleep(1)



def get_table(browser):
    table = browser.find_element_by_id("tblite_gp")
    trlist = table.find_elements_by_tag_name("tr")
    jj = []
    for row in trlist:
        conNum = 0
        while True:
            if title(browser,row,jj) or conNum > 10:
                break
            conNum = conNum + 1
    createAll(jj)

def title(browser,row,jj):
    try:
        tdlist = row.find_elements_by_tag_name("td")
        if len(tdlist) > 0:
            code = tdlist[0].text
            name = tdlist[1].text
            print(code + ":" + name)
            # jj_url = jj_url_str.format(code=code)
            # open_jj_detail(browser,jj_url)
            detail_url_end = detail_url.format(code=code)
            open_detail(browser, detail_url_end, code)
            o = Jjjin(code, name)
            jj.append(o)
    except:
        sleep(1)
        return False
    return True

# def open_jj_detail(browser,url):
#     print(url)
#     newwindow = 'window.open("{name}")'.format(name=url)
#     browser.execute_script(newwindow)
#     # 移动句柄，对新打开页面进行操作
#     browser.switch_to_window(browser.window_handles[1])
#     while browser.current_url.find("fund") == -1:
#         sleep(0.2)
#
#     table = browser.find_element_by_xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[2]/table/tbody')
#     trlist = table.find_elements_by_tag_name('tr')
#     td1 = trlist[0].find_elements_by_tag_name('td')
#     scale = td1[1].text
#     manager = td1[2].text
#
#     td2 = trlist[1].find_elements_by_tag_name('td')
#     create_time = td2[0].text
#     company = td2[1].text
#     print(scale + "\t" +manager + "\t" + create_time+ "\t" + company, end=" ")
#     # 关闭该新打开的页面
#     browser.close()
#     # 不关闭，要移动到上一个页面，我们要移动句柄
#     browser.switch_to_window(browser.window_handles[0])

def open_detail(browser,url,code):
    newwindow = 'window.open("{name}")'.format(name=url)
    browser.execute_script(newwindow)
    # 移动句柄，对新打开页面进行操作
    browser.switch_to_window(browser.window_handles[1])
    while browser.current_url.find("fundf10") == -1:
        sleep(0.2)
    # 具体操作
    try:
        all_buttion=browser.find_element_by_xpath('//*[@id="cctable"]/div[1]/div/div[3]/font/a')
        browser.execute_script("arguments[0].click();", all_buttion)
        sleep(1)
    except:
        print("没有多余的")
    try:
        table = browser.find_element_by_xpath('//*[@id="cctable"]/div[1]/div/table/tbody')
        #//*[@id="position_shares"]/div[1]/table/tbody
        trlist = table.find_elements_by_tag_name('tr')
        objs = []
        for row in trlist:
            tdlist = row.find_elements_by_tag_name("td")
            gu_code = tdlist[1].text
            gu_name = tdlist[2].text
            scale = tdlist[6].text
            obj = Gupiao(code,gu_name,gu_code,scale)
            objs.append(obj)
        createAll(objs)
    except:
        print("无股票")
    # 关闭该新打开的页面
    browser.close()
    # 不关闭，要移动到上一个页面，我们要移动句柄
    browser.switch_to_window(browser.window_handles[0])





if __name__ == "__main__":
    start_tt()

