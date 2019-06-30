# -*- coding: utf8 -*-

import json
from urllib.request import urlopen
import sys

def ranking(temp,r1,r2,r3,r4,r5,r6):
    if temp <= 25:
        num = int(round(temp/5,0))
        r1 = '='*num+ ' '*(5-num)
    elif temp <= 50:
        num = int(round((temp-25)/5,0))
        r1 = '='*5
        r2 = '='*num+ ' '*(5-num)
    elif temp <= 75:
        num = int(round((temp-50)/5,0))
        r1,r2 = '='*5,'='*5
        r3 = '='*num+ ' '*(5-num)
    elif temp <= 100:
        num = int(round((temp-75)/5,0))
        r1,r2,r3 = '='*5,'='*5,'='*5
        r4 = '='*num+ ' '*(5-num)
    elif temp <= 125:
        num = int(round((temp-100)/5,0))
        r1,r2,r3,r4 = '='*5,'='*5,'='*5,'='*5
        r5 = '='*num+ ' '*(5-num)
    elif temp <= 150:
        num = int(round((temp-125)/5,0))
        r1,r2,r3,r4,r5 = '='*5,'='*5,'='*5,'='*5,'='*5
        r6 = '='*num+ ' '*(5-num)

    print("[%s|%s|%s|%s|%s|%s]" % (r1,r2,r3,r4,r5,r6))
    print("0     25   50   75   100   125   150")

    
rsp=urlopen('https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000259/?format=csv&token=qm0+Vkjb6UOUg+XetUmKNg')
data=rsp.read()
csvdata=data.decode('utf-8')
csv=[]
csv=csvdata.splitlines()
i=0
dict1={}
for line in csv:
    if i>0:
        item=line.split(",")
        Sitename=item[0].strip('"')
        Country=item[1].strip('"')
        AQI=item[2].strip('"')
        MajorPollutant=item[3].strip('"')
        Status=item[4].strip('"')
        dict1[Sitename]=[AQI,Sitename,Country,MajorPollutant,Status]
    i+=1    
dict1=sorted(dict1.values(),reverse=True)
r1,r2,r3,r4,r5,r6=' '*5,' '*5,' '*5,' '*5,' '*5,' '*5

x=0
while x==0:
    print("=====即時空汙品質查詢=====")
    a=input("調查各地即時AQI濃度請按1\n調查區域空汙品質查詢請按2\n")
    if(int(a)==1):
        for w in range(1,i):
            if dict1[w-1][0]=="":
                break;
            temp=dict1[w-1][0]
            tempAQI=int(temp)
            print (json.dumps(dict1[w-1][0:4], ensure_ascii=False).strip('"'))
            ranking(tempAQI,r1,r2,r3,r4,r5,r6)
        print("\n")
            
    if(int(a)==2):
        b=input("輸入調查區域:")
        for w in range(1,i):
            c=dict1[w-1][1]
            if b==c:
                print ('空氣品質指標AQI｜'),json.dumps(dict1[w-1][0], ensure_ascii=False).strip('"')
                print ('區域｜'),json.dumps(dict1[w-1][1], ensure_ascii=False).strip('"')
                print ('城市｜'),json.dumps(dict1[w-1][2], ensure_ascii=False).strip('"')
                print ('氣體｜'),json.dumps(dict1[w-1][3], ensure_ascii=False).strip('"')
                print ('狀態｜'),json.dumps(dict1[w-1][4], ensure_ascii=False).strip('"')
                
    b=input("\n謝謝你的使用\n\n若要結束請按0\n若要繼續請按1\n")
    if(int(b)==0):
        print("\nGOODBYE!")
        x=1
    if(int(b)==1):
        x=0
        print("\n")        
