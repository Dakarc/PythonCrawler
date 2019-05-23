import re

# 匹配某个字符
text = "hello"
ret = re.match('he',text)
print(ret.group())