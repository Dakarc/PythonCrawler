from urllib import request,parse

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data = {
    'first':'true',
    'pn':1,
    'kd':'pyhton'
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
