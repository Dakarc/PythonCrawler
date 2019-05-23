import csv

with open('stu.csv','r',encoding='utf-8') as fp:
    # reader是一个迭代器
    reader = csv.reader(fp)
    for x in reader:
         name = x['头1']
         print(name)

# 测试