from  urllib import request
from urllib import parse
url1 = "http://www.baidu.com/s?wd=123"
# url = parse.urlparse(url1)
url = parse.urlsplit(url1)
print(url)
# print("schene:",url.scheme)