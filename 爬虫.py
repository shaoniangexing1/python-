import requests
import re#正则表达式
#爬取图片
url="http://www.people.com.cn/"
html=requests.get(url)#获得url源代码
# print(html.text)#.text爬取网页全部信息
regrule=r'<img src=".*?.jpg'#.*?所有的一<img src="开头.jpg结尾的#定义正则
imgre=re.compile(regrule)#编译正则表达式
urls=imgre.findall(html.text)#利用正则查找所有满足要求的连接（列表形式）
# print(urls)
x=1
for imgu in urls:
    spli=re.split('''<img src="''',imgu)#分隔字符串('''<img src="'''将<img src="转为空)
    flo=requests.get(url+spli[1])#绝对路径和相对路径连接
    filename="E:/图片/1/%d.jpg"%x#新建图片文件
    f=open(filename,"wb")#设置文件读写
    filesize=f.write(flo.content)
    x+=1

















