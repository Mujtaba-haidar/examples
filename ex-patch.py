import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/10'
respon = requests.get(api_url)
print(respon.status_code)
print(respon.json())

todo = {"title":"wash car"}
respon = requests.patch(api_url,json=todo)
print(respon.status_code)
print(respon.json())
print(r'foo\\bar\nbaz')