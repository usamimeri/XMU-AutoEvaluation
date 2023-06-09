import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
'''经院老师助教我爱你程序,对热情敬业的老师同学评最高分！'''


def evaluate():
    def get_name(source):
        form=re.findall(r'<div class="grid-view">(.*?)</div>',source,re.DOTALL)[0] 
        name_list=re.findall(r'<a[^>]*>(.*?)</a>',form)
        return name_list
    driver=webdriver.Chrome() #需要安装对应版本的谷歌驱动
    driver.get('https://course.soe.xmu.edu.cn')
    we=driver.find_element(by=By.CSS_SELECTOR,value='img[src="/Themes/Shared/Images/xmu_logon.png"]')
    we.click() #点击厦大登录
    time.sleep(1)
    we=driver.find_element(By.CSS_SELECTOR,"#userNameLogin_a")
    we.click()
    time.sleep(1)
    we=driver.find_element(By.CSS_SELECTOR,'#username')
    we.send_keys(USERNAME)
    we=driver.find_element(By.CSS_SELECTOR,'#password')
    we.send_keys(PASSWORD)
    we=driver.find_element(By.CSS_SELECTOR,'#login_submit')
    we.click()
    time.sleep(2)
    we=driver.find_element(by=By.CSS_SELECTOR,value='img[src="/IconFiles/20151105111857224.png"]')
    we.click() #点击两院评估
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    source=driver.page_source #获取网页源码
    name_list=get_name(source) #教师和助教名单
    time.sleep(2)
    for name in name_list:
        we=driver.find_element(By.LINK_TEXT,name)
        we.click()
        time.sleep(1)
        all_buttons=driver.find_elements(By.CSS_SELECTOR,'input[value="5"][type="radio"]')
        for i in all_buttons:
            i.click()
            time.sleep(0.3)
        time.sleep(1)
        we=driver.find_element(By.LINK_TEXT,'保存')
        we.click()
        time.sleep(1)
    print('成功完成自动评价')

if __name__ == '__main__':
    USERNAME='学号' #你的学号
    PASSWORD='密码' #你的密码
    evaluate()



