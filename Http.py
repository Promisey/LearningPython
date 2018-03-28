# coding=utf-8
import http.client, re

'''
conn = http.client.HTTPConnection("www.example.com")
conn.request("GET","/")
response = conn.getresponse()

print(response.status,response.reason)
content = response.read().decode()
# content = content.split("\r\n")
print(content)

'''
conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET","/vamei")
response = conn.getresponse()

print(response.status,response.reason)
content = response.read().decode()
content = content.split("\r\n")

# pattern = "posted @ (\d{4}-[0-1]\d-[0-3]\d [0-2]\d:[0-6]\d) Vamei 阅读\((\d+)\) 评论"
pattern1 = "posted @ (\d{4}-[0-1]\d-[0-3]\d [0-2]\d:[0-6]\d) Vamei 阅读\((\d+)\) 评论"
print(content)

for line in content:
    m = re.search(pattern1, line)
#    print(m)
    if m != None:
        print(m.group(1))


a = "posted @ 2018-03-04 22:28 Vamei 阅读(570) 评论(1)"
b = re.search(pattern1, a)
print(b.group(1),b.group(2))