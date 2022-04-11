import requests

endpoint = "https://httpbin.org/status/200/"
endpoint  = "https://httpbin.org/anything"

get_response  = requests.get(endpoint) #http request
print(get_response.json())