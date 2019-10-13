import time
from selenium import webdriver
import requests
import xlrd
import xlwt
####获取500网站，双色球2019年数据
def login():
    myworkbook = xlwt.Workbook()
    myworksheet = myworkbook.add_sheet('double')

    driver = webdriver.Chrome()
    url = 'http://datachart.500.com/ssq/?expect=all&from=19001&to=19107&jumpsrc=http://datachart.500.com/ssq/'
    driver.get(url)
    time.sleep(3)
    driver.minimize_window()
    # 使用CSSSelector正则匹配头部
    elems = driver.find_elements_by_xpath("//tbody[@id='tdata']/tr//td[@class='chartBall01']|//td[@class='chartBall01 chartBall07']|//td[@class='chartBall02']|//td[@align='center']")
    j=0
    i=0
    for elem in elems:

        #j=j+1
        #print(j,i,elem.text)
        #print(elem.text[0:3])
        if elem.text[0:3]=='190' or  elem.text[0:3]=='191':
            j=j+1
            i=0
        myworksheet.write(j, i, elem.text)
        i=i+1
        # if i>=10:
        #     exit()
        #print(elem.text)
    # 163登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe
    myworkbook.save('d:/double.xls')
    driver.quit()


if __name__ == '__main__':
    login()
