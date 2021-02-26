#导包
from selenium import webdriver             #selenium包
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()               #打开浏览器
# driver.get("http://www.baidu.com")         #打开网页
driver.get("https://xdclass.net")
print(driver.title)                        #答应当前title或url
print(driver.current_url)

sleep(2)
#1、hover定位鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
ActionChains(driver).move_to_element(menu_ele).perform()    #对定位到的元素执行鼠标移动到上面的操作
#选中子菜单
sub_menu_ele = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(1)")
sleep(2)
sub_menu_ele.click()
sleep(2)


#2、模拟用户登录  查找登录框>输入用户名密码>点击登录>判断是否登录成功>打印结果
#找到登录按钮并点击
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
ActionChains(driver).click(login_ele).perform()

#查找输入框，输入账号密码，输入框需要提前清空
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("18983663348")
sleep(1)
driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("he3324430340")
sleep(1)
driver.find_element_by_css_selector(".btn").click()
sleep(2)    #不设置等待时间会导致后面捕获不到元素

#判断是否登录成功
user_info_ele = driver.find_element_by_css_selector(".avatar_img")
sleep(1)
ActionChains(driver).move_to_element(user_info_ele).perform()    #触发hover事件，检查账户名
#获取用户名元素
user_name_ele = driver.find_element_by_css_selector(".username")
print("------测试结果------")
print(user_name_ele.text)

name = user_name_ele.text

if name == u"秋天的土豆":            #中文字符需加一个u
    print("login ok")
else:
    print("login faile")

