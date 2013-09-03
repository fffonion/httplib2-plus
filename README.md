httplib2-plus Document
========

What's different in this version?

##Add chunk read support

Usage:
```python
import httplib2
def my_call_back(has_read,total):#the callback hook func
	print ("%d %d %f" %(has_read,total,has_read*100.0/total))
http=httplib2.Http()
resp,content=http.request('http://www.google.com/',callback_hook=my_call_back)#use callback_hook= to define a func
```

Additionally, you can specify a callback_hook and set chunk_size to None to make "every request like HEAD". Sometimes it may be useful.
(I have no idea whether socket pool inside httplib2 can reuse this connection. Maybe yes.)
The following example make a POST request closed before retriving any contents.
```python
>>>import httplib2
>>>http=httplib2.Http()
>>>resp,content=http.request('http://www.baidu.com/',method='GET',callback_hook=lambda x:x,chunk_size=None)
>>>len(content)
0
>>>resp,content=http.request('http://www.baidu.com/',method='POST')
>>>len(content)
160
>>>resp,content=http.request('http://www.baidu.com/',method='POST',callback_hook=lambda x:x,chunk_size=None)
>>>len(content)
0
```


##fix proxy bugs

httplib2 does not check registry for proxy settings. It only check the environment vars.
In httplib2-plus this is solved. Using "urllib.getproxies()"

##forked from the version 0.8
