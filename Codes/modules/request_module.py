# Request Module
# For handle api


import requests

# for get request
# response = requests.get("https://www.google.com")
# print(response.text)


# for post request

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Bilal",
    "body": 'bar',
    "userId":'1'
}

headers = {
    'Content-type':"application/json;charset=UTF-8"
}

response = requests.post(url,headers=headers,json=data)

print(response.text)



