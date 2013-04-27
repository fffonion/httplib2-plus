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

##fix proxy bugs

httplib2 does not check registry for proxy settings. It only check the environment vars.
In httplib2-plus this is solved. Using "urllib.getproxies()"

##forked from the version 0.8