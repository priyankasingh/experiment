import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'http://google.com')
c.perform() 
