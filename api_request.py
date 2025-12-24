import requests #library that lets you to send request through python to web servers
from colorama import Fore, Style, init


url = "https://www.ibm.com/"
r=requests.get(url)
if r.status_code==200:
    print(f"status code is {r.status_code} - {Fore.GREEN}PASSED{Style.RESET_ALL}")
else:
    print(f"status code is {r.status_code} - {Fore.RED}FAILED{Style.RESET_ALL}")
'''
r.request.headers - you can view request headers
print("____\n", r.request.body) - requesst body as well - which was empty in our case
r.headers - shows HTTP response headers using attribute headers - returns python dict for http response headers
you can look at the dictionary values here.
you can receive the specific info by using the key. example:
'''
# headers_dict=r.headers
# print(headers_dict)
# print(headers_dict['date'])
# print(headers_dict['Content-Type']) #- the type of content of the data
# print(r.encoding) #check encoding code
# print(r.text[0:100]) # display the html text in the body, review the first 100 characters.

url_get="http://httpbin.org/get" #adding get in the end to perform get request
#create a query string
payload={"name": "Joseph", "ID":"123"}
r=requests.get(url_get, params=payload)
# print(r.url)
# print(r.request.body)
# print(r.status_code)
# print(r.text)
# print(r.headers['Content-Type'])
# print(r.json()) #- format the json type response
# print(r.json()['args']) # - name and values for the query string

'''
Post request send the data using the data body, not the url - you need to add what you want to send in request body.
'''
url_post="http://httpbin.org/post" # adding post instead of get means after accesing to the url, it'll wait to get the data, not respond
r_post=requests.post(url_post, data=payload)
print("POST Request URL:", r_post.url)
print("GET Request URL:", r.url)
print("post request body:", r_post.request.body)
print("get request body:", r.request.body)
print(r_post.json()['form']) # get the payload dict info