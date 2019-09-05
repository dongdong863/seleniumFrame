#coding:utf-8
#利用分割网址的方法来取
def GetUrl(url):
    urls = url.split('/')
    url = urls[0]+'/'+urls[1]+'/'+urls[2]+'/'+urls[3]+'/'

    return url

print(GetUrl('https://www.cnblogs.com/111testing/p/9609105.html'))