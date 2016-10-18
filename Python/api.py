'''
pip install requests

Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE)
HTTP Status Codes (http://www.restapitutorial.com/httpstatuscodes.html)
    - 1x Informational
    - 200 OK
    - 3xx Redirection
    - 4xx Client Error 
        - 400 Bad Request
        - 404 Not found
    - 5xx Server Error 
        - 500 Internal Server Error

Testing endpoints: http://httpbin.org/get
'''

import requests

resp = requests.get('http://httpbin.org/get')
print resp.json()['origin']
print '\n'

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.json()['args']
print r.url

r = requests.put("http://httpbin.org/put")
print r 
print '\n'
r = requests.delete("http://httpbin.org/delete")
print r 
print '\n'
r = requests.head("http://httpbin.org/get")
print r 
print '\n'
r = requests.options("http://httpbin.org/get")
print r
print '\n'

