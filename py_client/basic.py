
import requests

#endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json = {"title": "Abc123", "content":"Hello World!", 
"price": "abc1234" }) # HTTP Request
# print(get_response.text) # print raw response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP REQUEST -> JSON
print(get_response.json()) 
# print(get_response.status_code)

print("This is a branch test")