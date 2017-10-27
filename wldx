import os
import re
import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#selenium IE的程序调用
iedriver= "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"]=iedriver

#调用IE
driver=webdriver.Ie(iedriver)
#考试页面
driver.get("http://wldx.sgcc.com.cn:8080/lms/user/topic.htm?id=6108571_8a8128a15b52c323015b7b1e26ce1a9a&usercard=44ebd5946d956b0c064a57a57ec659f7&random=1505789045000")
#加载时间3秒，用来保证IE页面的脚本加载完成
time.sleep(3)
#网页源码并将 “_" 替换为空格。
wen_ti=driver.page_source.replace("_"," ")
#关闭IE驱动，减少占用
driver.close()
#正则匹配，从源码中提取问题字符串
wenti=re.findall(r"<DIV class=TMTitle>(.+?) <INPUT",wen_ti)

#输入excel题库文件
data=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\11.xlsx')

table=data.sheets()[0]
#提取行数
nrows=table.nrows
#定义存放问题和答案的dict
dataresult=[]
result=[]
#将每一行的内容存入dict
for i in range(nrows):
    dataresult.append(table.row_values(i))
#提取dataresult中的列表内容，并把i【0】和 wenti列表匹配
for i in dataresult :   
    if (i[0]) in wenti:
        print (i)
