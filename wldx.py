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
driver.get("考试页面URL")
#加载时间30秒，用来保证IE页面的脚本加载完成
time.sleep(5)
#网页源码并将 “_" 替换为空格,引号替换为英文

wen_ti=driver.page_source.replace(" ","").replace("“","\"").replace("”","\"")
#print (wen_ti)
#关闭IE驱动，减少占用
#driver.close() 
#正则匹配，从源码中提取问题字符串 TMTitle_1
wenti=re.findall(r"\">(.+?)<INPUT",wen_ti)
#print (wenti)
#输入excel题库文件，答案格式第一列必须是问题，
data=xlrd.open_workbook(r'答案路径')

table=data.sheets()[0]
#提取行数
nrows=table.nrows
#定义存放问题和答案的dict
dataresult=[]
result=[]
#将每一行的内容存入dict
for i in range(nrows):
    dataresult.append(table.row_values(i))
#print (dataresult)
#提取dataresult中的列表内容，并把i【0】和 wenti列表匹配
for i in wenti :
    print ("************************")
    shu_mu=0
    if i == (dataresult[shu_mu][0]):
        print (dataresult[shu_mu])
        break
    else:
        shu_mu+=1
