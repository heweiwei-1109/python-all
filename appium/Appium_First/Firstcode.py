from appium import webdriver

desired_caps = {}
desired_caps["platformName"] = "Android"   #操作系统
#模拟器设备
desired_caps["deviceName"] = "127.0.0.1:62025"    #设备名
desired_caps["platformVersion"] = "5.1.1"       #手机系统版本
#真机


desired_caps["app"] = r'C:\Users\hewei\Desktop\kaoyan3.1.0.apk'      #安装包路径
desired_caps["appPackage"] = "com.tal.kaoyan"          #包名
desired_caps["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"    #等待启动的 Android Activity 名称

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("jieshu")