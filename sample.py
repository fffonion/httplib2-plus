#coding:utf-8
import httplib2,urllib
def hooker(chunksize,getsize):
    print chunksize,getsize,'get chunk'
h = httplib2.Http(callback_hook=hooker,chunk_size=8192)
#h = httplib2.Http()
#url="http://ios.roame.net/files/6GwXTv@go@qQolTldxiQN4v8imcB2c1gos8N7o9TmU@f89h0fDhCnI78blZQ/ROAME_263941_313927C0.jpg"
url="http://www.roame.net"
resp, content = h.request(url)
print resp
print len(content)
url="http://ios.roame.net/files/C@3GXJTWqymuoD8WgQZIdQzDHvn9K@FVpm9ibFe6qrIHIYyofewV6JiYV/ROAME_263757_AD070752.jpg"
resp, content = h.request(url,headers={'connection':'keep-alive'})
print resp['content-length']
print len(content)