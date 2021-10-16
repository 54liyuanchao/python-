import requests
from lxml import etree

#创建session对象
session = requests.session()
header = {
    'user-agent': 'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)'
}
get_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
r = session.get(url=get_url, headers=header)


#XPath解析隐藏域
html = etree.HTML(r.text)

VIEWSTATE = html.xpath('//*[@id="__VIEWSTATE"]/@value')
print(VIEWSTATE[0])

VIEWSTATEGENERATOR = html.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')
print(VIEWSTATEGENERATOR[0])

#获取验证码
imgUrlList = html.xpath('//*[@id="imgCode"]/@src')
imgUrl = "https://so.gushiwen.cn/"+imgUrlList[0]
print(imgUrl)
res = session.get(imgUrl)
with open('code.jpg', 'wb') as f:
    f.write(res.content)

code = input('输入验证码')


#登录请求
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1161961146@qq.com',
    'pwd': '0ooo00ooo0',
    'code': code,
    'denglu': '登录'
}
response = session.post(url=post_url, headers=header, data=data)
print(response.text)