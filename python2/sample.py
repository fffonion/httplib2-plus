#coding:utf-8
import httplib2,urllib
def hooker():
    print 'get chunk'
h = httplib2.Http(callback_hook=hooker,chunk_size=1000)
#h = httplib2.Http()
resp, content = h.request("http://www.roame.net")
print resp
print len(content)