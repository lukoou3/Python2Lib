# encoding=utf8

import urllib, urllib2
import json
import pprint

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }

def test_get():
    url = 'http://127.0.0.1:8000/get?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    print urllib.urlencode(params)
    request = urllib2.Request(url=url+"&" + urllib.urlencode(params), headers=headers)
    response = urllib2.urlopen(request, timeout=20)
    ret = response.read()
    print ret
    print str(ret)
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def test_post():
    url = 'http://127.0.0.1:8000/post?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    request = urllib2.Request(url=url, data= urllib.urlencode(params), headers=headers)
    response = urllib2.urlopen(request, timeout=20)
    ret = response.read()
    print ret
    print str(ret)
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def test_post_json():
    url = 'http://127.0.0.1:8000/post?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    json_headers = headers.copy()
    json_headers.update({"Content-Type": 'application/json'})
    request = urllib2.Request(url=url, data= json.dumps(params), headers=json_headers)
    response = urllib2.urlopen(request, timeout=20)
    ret = response.read()
    print ret
    print str(ret)
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def test_http_post():
    url = 'http://127.0.0.1:8000/post?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    response = http_post(url, params)
    ret = response.read()
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def test_http_post_json():
    url = 'http://127.0.0.1:8000/post?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    response = http_post(url, params, is_json=1)
    ret = response.read()
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def test_http_put():
    url = 'http://127.0.0.1:8000/put?name=小明&age=17'
    params = {'name2': '小花', 'age2': 20}
    response = http(url, method='PUT',data=params, is_json=1)
    ret = response.read()
    pprint.pprint(json.loads(ret))
    data = json.loads(ret)
    print data['query']['name']

def http_get(url, params=None, headers={}, timeout=20):
    if params is not None:
        if '?' in url:
            url = url + "&" + urllib.urlencode(params)
        else:
            url = url + "?" + urllib.urlencode(params)
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request, timeout=timeout)
    return response

def http_post(url, data, is_json=False, headers={}, timeout=20):
    if is_json:
        headers = headers.copy()
        headers.update({"Content-Type": 'application/json'})
        data = json.dumps(data)
    else:
        data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data, headers=headers)
    response = urllib2.urlopen(request, timeout=timeout)
    return response

def http(url, method='GET', params=None, data=None, is_json=False, headers={}, timeout=20):
    if params is not None:
        if '?' in url:
            url = url + "&" + urllib.urlencode(params)
        else:
            url = url + "?" + urllib.urlencode(params)
    if data:
        if is_json:
            headers = headers.copy()
            headers.update({"Content-Type": 'application/json'})
            data = json.dumps(data)
        else:
            data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data, headers=headers)
    request.get_method = lambda: method
    response = urllib2.urlopen(request, timeout=timeout)
    return response

if __name__ == '__main__':
    #test_get()
    #test_post()
    #test_post_json()
    #test_http_post()
    test_http_post_json()