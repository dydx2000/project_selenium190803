#encoding:utf-8
import uiautomator2 as u2
d = u2.connect_wifi()
d.click()





print("hello world")


a = int(input("请输入A: \n"))
if a == 10:
    print("right")
else:
    print("wrong")