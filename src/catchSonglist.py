from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import csv

url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
#用phantomJS创建一个selenium的webdriver
#driver = webdriver.PhantomJS()

if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')  # 无头参数
    driver = Firefox(executable_path='E:\pycharm\bin\geckodriver', firefox_options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径
    wait = WebDriverWait(driver, timeout=10)
    driver.get(url)
    wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
    print(driver.page_source)
    #准备存储歌单的csv
    csv_file = open("songlist.csv", "w", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(["标题", "播放数", "链接"])

    #解析每一页，直到下一页为空
    while url != "javascript:void(0)":
      driver.get(url) #用webdriver加载界面
      driver.switch_to.frame("contentFrame")#切换到内容的iframe
      data = driver.find_element_by_id("m-li-container").find_element_by_tag_name("li")#定位歌单标签

    for i in range(len(data)):#解析一页中的所有歌单
        #获取播放数
        nb = data[i].find_element_by_class_name("nb").text
        if "万" in nb and int(nb.spit("万")[0]) > 500:
            #获取播放数大于500万的歌单的封面
            msk = data[i].find_element_by_css_selector("a.msk")
            #把封面上的标题和链接连同播放数一起写到文件中
            writer.writerow([msk.get_attribute("title"),nb,msk.get_attribute("href")])
    #定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")
    csv_file.close()
    driver.quit()





